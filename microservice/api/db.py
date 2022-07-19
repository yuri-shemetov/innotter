import boto3
from . import local_settings


database = boto3.resource(
    'dynamodb',
    region_name='us-east-1',
    aws_access_key_id=local_settings.AWS_ACCESS_KEY_ID_DB,
    aws_secret_access_key=local_settings.AWS_SECRET_ACCESS_KEY_DB
)


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
