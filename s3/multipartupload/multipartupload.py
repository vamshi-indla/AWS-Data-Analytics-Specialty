"""
Usage:
    python multipartupload.py -f file1.mov at\ 22.17.57.mp4 -b vkis3books -cs 5 -p 4
"""
import boto3
import argparse
import multiprocessing
import json
import time

# Starts Multipart Upload
def start_upload(bucket, key):
    s3_client =  boto3.client('s3')

    response = s3_client.create_multipart_upload(
        Bucket = bucket,
        Key = key
        )
    
    return response['UploadId']


# Add Upload Part
def add_part(proc_queue, body, bucket, key, part_number, upload_id):
    s3_client = boto3.client('s3')

    response = s3_client.upload_part(
            Body = body,
            Bucket = bucket,
            Key = key,
            PartNumber = part_number,
            UploadId = upload_id
    )

    print(f"Finished Part: {part_number}, ETag: {response['ETag']}")
    proc_queue.put({'PartNumber': part_number, 'ETag': response['ETag']})
    return

# End Multipart Upload
def end_upload(bucket, key, upload_id, finished_parts):
    s3_client = boto3.client('s3')

    response = s3_client.complete_multipart_upload(
        Bucket = bucket, 
        Key = key, 
        MultipartUpload = {
            'Parts' : finished_parts,
        },
        UploadId = upload_id
    )

    return response

# Primary logic
def main():
    parser = argparse.ArgumentParser(description="Multipart upload")
    parser.add_argument('-f', '--file', type=str, required=True, help="File to upload")
    parser.add_argument('-b', '--bucket', type=str, required=True, help="S3 bucket to upload")
    parser.add_argument('-cs', '--chunk_size', type=int, required=True, help="Chunk size must be >5MiB", choices=range(5,101))
    parser.add_argument('-p', '--processors', type=int, default=10, choices=range(1,256), help="Number of processors to run simultaneously")
    args = vars(parser.parse_args())

    key = file = args['file']
    bucket = args['bucket']
    sim_proc = args['processors']
    upload_id = start_upload(bucket, key)
    print(f'Starting upload: {upload_id}')

    file_upload = open(file, 'rb')
    part_procs = []
    proc_queue = multiprocessing.Queue()
    queue_returns = []
    chunk_size = args['chunk_size'] * 1024 * 1024
    part_num = 1
    chunk = file_upload.read(chunk_size)

    while len(chunk) > 0:
        proc = multiprocessing.Process(target=add_part, args=(proc_queue, chunk, bucket, key, part_num, upload_id))
        part_procs.append(proc)
        part_num += 1
        chunk = file_upload.read(chunk_size)

    part_procs = [part_procs[i * sim_proc:(i + 1) * sim_proc] for i in range((len(part_procs) + (sim_proc - 1)) // sim_proc)]

    for i in range(len(part_procs)):
        for p in part_procs[i]:
            p.start()

        for p in part_procs[i]:
            p.join()

        for p in part_procs[i]:
            queue_returns.append(proc_queue.get())

    print(queue_returns)
    queue_returns = sorted(queue_returns, key=lambda i: i['PartNumber'])
    response = end_upload(bucket, key, upload_id, queue_returns)
    print(json.dumps(response, sort_keys=True, indent=4))




if __name__ == "__main__":
    start = time.time()
    main()
    print(f'Elapsed Time: %.2f seconds {time.time() - start}')
