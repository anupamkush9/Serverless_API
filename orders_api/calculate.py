import json
def calculator(event, context):
    event_body = json.loads(event.get('body'))
    total = sum([i for i in event_body['numbers']])
    return {"body": {"total": total}}