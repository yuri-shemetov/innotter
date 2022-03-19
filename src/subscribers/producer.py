import pika
from proj.local_settings import CELERY_BROKER_URL

params = pika.URLParameters(CELERY_BROKER_URL)

connection = pika.BlockingConnection(params)

channel = connection.channel()

def follower():
    channel.basic_publish(exchange='', routing_key='admin', body='Hello!')