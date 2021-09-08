from faker import Faker
import boto3
import argparse
import json

fake = Faker()

# get arguments from CLI
parser = argparse.ArgumentParser(description="Provide queuename and number \
            of records")
parser.add_argument("--queuename", type=str, help="queue name")
parser.add_argument("--records", type=int, help="number of records")
args = parser.parse_args()
print(args.queuename, args.records)


# Get the service resource
sqs_client = boto3.resource('sqs')

# Get the Queue name
queue = sqs_client.get_queue_by_name(QueueName=args.queuename)


for count in range(args.records):
    payload = {}
    payload['request'] = fake.name()
    payload['response'] = fake.text()

    response = queue.send_message(
                MessageBody=json.dumps(payload),
                MessageGroupId="Dead-Letter-Queue-Group"
                )
    print(response.get('MessageId'))
