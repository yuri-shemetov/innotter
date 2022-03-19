# from curses import keyname
from api.models import CounterIn, CounterOut, CounterUpdate
from api.db import table, database
from botocore.exceptions import ClientError


def get_counter(page, dynamodb=None):
    if not dynamodb:
        dynamodb = database
    try:
        response = table.get_item(Key={'page': page})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']


def add_counter(payload: CounterIn):
    response = table.put_item(
        Item={
            'page': payload.page,
            'counters': {
                'count_follower': payload.count_follower,
                'count_follow_request':  payload.count_follow_requests
                }
            }
    )
    return response


# async def get_all_counters(page):
#     table = database.Table('info_page')
#     try:
#         response = table.get_item(Key={'page': page})
#     except ClientError as e:
#         print(e.response['Error']['Message'])
#     else:
#         return response['Item']


def update_counter(page, count_follow_requests, count_follower, dynamodb=None):
    if not dynamodb:
        dynamodb = database
        response = table.update_item(
            Key={'pade': page},
            UpdateExpression="set counters.count_follower=:f, counters.count_follow_requests=:r",
            ExpressionAttributeValues={
                ':f': count_follower,
                ':r': count_follow_requests,
            },
            ReturnValues="UPDATED_NEW"
        )
    return response

# async def delete_counter(id: int):
#     query = movies.delete().where(movies.c.id==id)
#     return await database.execute(query=query)

def delete_counter(id: int):
    try:
        response = table.delete_item(
        Key={'page': id}
        )
    except ClientError as e:
        if e.response['Error']['Code'] == "ConditionalCheckFailedException":
            print(e.response['Error']['Message'])
        else:
            raise
    else:
        return response
