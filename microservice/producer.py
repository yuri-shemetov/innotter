import pika, json
from api.local_settings import CELERY_BROKER_URL

params = pika.URLParameters(CELERY_BROKER_URL)

connection = pika.BlockingConnection(params)

channel = connection.channel()

def follower(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(
        exchange='',
        routing_key='src',
        body=json.dumps(body),
        properties=properties
    )