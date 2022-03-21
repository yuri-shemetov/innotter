import pika, json
from proj.local_settings import CELERY_BROKER_URL
from pages.models import Page


params = pika.URLParameters(CELERY_BROKER_URL)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='src')

def callback(ch, method, properties, body):
    print('Recived in src')
    id = json.loads(body)
    print(id)
    page = Page.objects.get(id=id)
    page

channel.basic_consume(queue='src', on_message_callback=callback, auto_ack=True)

print('Started consuming')

channel.start_consuming()

channel.close()