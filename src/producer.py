import pika, json
from proj.local_settings import BROKER_URL_FOR_DB

params = pika.URLParameters(BROKER_URL_FOR_DB)

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(
        exchange='',
        routing_key='microservice',
        body=json.dumps(body),
        properties=properties
    )
