import json

import boto3
from boto3.dynamodb.conditions import Key


class InvalidResponse(Exception):
    def __init__(self, status_code):
        self.status_code = status_code


# Don't modify this function name and arguments
def query_user_notes(user_email):
    dynamo_db = boto3.resource('dynamodb')
    user_notes_table = dynamo_db.Table('user-notes')

    filtering_exp = Key('user').eq(user_email)
    result = user_notes_table.query(
        KeyConditionExpression=filtering_exp,
        ScanIndexForward=False,
        Limit=10
    )
    return result['Items']


# Don't modify this function name and arguments
def get_authenticated_user_email(token):
    dynamo_db = boto3.resource('dynamodb')
    tokens_table = dynamo_db.Table('token-email-lookup')

    # Validate the given token with one from the database
    response = tokens_table.get_item(Key={
        "token": token,
    })

    if 'Item' not in response:
        return ""
    return response['Item']['email']


def authenticate_user(headers):
    authentication_header: str = headers.get('Authentication')

    if not authentication_header or not authentication_header.startswith("Bearer "):
        # Auth token is missing or malformed
        raise InvalidResponse(400)

    token = authentication_header.split("Bearer ")[1]
    if not token:
        # token is empty
        raise InvalidResponse(403)

    # Validate the Authentication header
    user_email = get_authenticated_user_email(token)
    if not user_email:
        # token is invalid. Raise error here as internal implementations may change
        raise InvalidResponse(403)

    return user_email


def build_response(status_code, body=None):
    result = {
        'statusCode': str(status_code),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
        },
    }
    if body is not None:
        result['body'] = body

    return result


# Don't modify handler, make other functions feet it
def handler(event: dict, context):
    try:
        user_email = authenticate_user(event['headers'])
        notes = query_user_notes(user_email)
    except InvalidResponse as e:
        return build_response(status_code=e.status_code)
    else:
        return build_response(
            status_code=200,
            body=json.dumps(notes)
        )
