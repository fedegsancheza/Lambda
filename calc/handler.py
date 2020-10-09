import json


def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': int(event["op1"])+int(event["op2"])
    }
