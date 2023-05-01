import json

def lambda_handler(event, context):
    order = {'id':123, 'name':'this is test order'}
    return {
        'statusCode': 200,
        'headers': {},
        'body': json.dumps(order)
    }