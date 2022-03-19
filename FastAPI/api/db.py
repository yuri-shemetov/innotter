import boto3
# from . import local_settings

# Get the service resource.
database = boto3.resource(
    'dynamodb',
    region_name='us-east-1',
    aws_access_key_id='AKIAUKWJS7Z3UALCNHVH',
    aws_secret_access_key='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')


def create_table():
    database.create_table(
        TableName='info_page',
        KeySchema=[
            {
                'AttributeName': 'page',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'page',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )

table = database.Table('info_page')
table.put_item(
   Item={
        'page': 'my_page',
        'counters': {
            'count_follower': 1,
            'count_follow_requests': 0
        }
    }
)

# table_name = 'trial'

# dynamodb_client = boto3.client(
#     'dynamodb',
#     region_name='us-east-1',
#     aws_access_key_id='AKIAUKWJS7Z3UALCNHVH',
#     aws_secret_access_key='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'   
# )


# item_scarface = {
#     'Title': {'S':'first'},
#     'Year': {'S':'1990'}
# }

# if __name__ == '__main__':
#     dynamodb_client.put_item(TableName = table_name, Item = item_scarface)
