import json

def lambda_handler(event, context):
    print(f"Received event\n{event}")

    rec_length = len(event['Records'])
    for i, record in enumerate(event['Records']):
        if i < 2:
            print(f"{record['body']}")
        else:
            raise Exception("Printed 2 records and then errored out. Check SQS Queue")

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
