import json
import base64


def lambda_handler(event, context):
    # TODO implement

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda! modify Git Action!! by jay add IAM lambda access')
    }