from api.db import table, database
from botocore.exceptions import ClientError


def get_everything_counter(dynamodb=None):
    if not dynamodb:
        dynamodb = database
    response = table.scan(AttributesToGet=['page', 'counters'])
    return response['Items']


def get_counter(page, dynamodb=None):
    if not dynamodb:
        dynamodb = database
    try:
        response = table.get_item(Key={'page': page})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']


def add_counter(page, count_follow_requests, count_follower, dynamodb=None):
    if not dynamodb:
        dynamodb = database
    response = table.put_item(
        Item={
            'page': page,
            'counters': {
                'count_follower': count_follower,
                'count_follow_requests': count_follow_requests
                }
            }
    )
    return response


def update_counter(page, count_follow_requests, count_follower, dynamodb=None):
    if not dynamodb:
        dynamodb = database
    response = table.update_item(
        Key={'page': page},
        UpdateExpression="set counters.count_follower=:f, counters.count_follow_requests=:r",
        ExpressionAttributeValues={
            ':f': count_follower,
            ':r': count_follow_requests,
        },
        ReturnValues="UPDATED_NEW"
    )
    return response


def delete_counter(page, dynamodb=None):
    if not dynamodb:
        dynamodb = database
    try:
        response = table.delete_item(
            Key={'page': page}
        )
    except ClientError as e:
        if e.response['Error']['Code'] == "ConditionalCheckFailedException":
            print(e.response['Error']['Message'])
        else:
            raise
    else:
        return response


def increase_count_followers(page, dynamodb=None):
    if not dynamodb:
        dynamodb = database
    response = table.update_item(
        Key={'page': page},
        UpdateExpression="SET counters.count_follower = counters.count_follower + :num",
        ExpressionAttributeValues={
            ":num": 1
        },
        ReturnValues="UPDATED_NEW"
    )
    return response


def increase_count_follow_requests(page, dynamodb=None):
    if not dynamodb:
        dynamodb = database
    response = table.update_item(
        Key={'page': page},
        UpdateExpression="SET counters.count_follow_requests = counters.count_follow_requests + :num",
        ExpressionAttributeValues={
            ":num": 1
        },
        ReturnValues="UPDATED_NEW"
    )
    return response


def decrease_increase(page, dynamodb=None):
    if not dynamodb:
        dynamodb = database
    response = table.update_item(
        Key={'page': page},
        UpdateExpression="SET counters.count_follow_requests = counters.count_follow_requests - :num, counters.count_follower = counters.count_follower + :num",
        ExpressionAttributeValues={
            ":num": 1
        },
        ReturnValues="UPDATED_NEW"
    )
    return response


def decrease_count_follow_requests(page, dynamodb=None):
    if not dynamodb:
        dynamodb = database
    response = table.update_item(
        Key={'page': page},
        UpdateExpression="SET counters.count_follow_requests = counters.count_follow_requests - :num",
        ExpressionAttributeValues={
            ":num": 1
        },
        ReturnValues="UPDATED_NEW"
    )
    return response


def decrease_count_follower(page, dynamodb=None):
    if not dynamodb:
        dynamodb = database
    response = table.update_item(
        Key={'page': page},
        UpdateExpression="SET counters.count_follower = counters.count_follower - :num",
        ExpressionAttributeValues={
            ":num": 1
        },
        ReturnValues="UPDATED_NEW"
    )
    return response


def delete_followers(page, dynamodb=None):
    if not dynamodb:
        dynamodb = database
    response = table.update_item(
        Key={'page': page},
        UpdateExpression="SET counters.count_follower = :num",
        ExpressionAttributeValues={
            ":num": 0
        },
        ReturnValues="UPDATED_NEW"
    )
    return response
