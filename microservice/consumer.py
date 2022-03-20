import pika, json
from api import models, db_manager, local_settings

params = pika.URLParameters(local_settings.CELERY_BROKER_URL)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='microservice')

def callback(ch, method, properties, body):
    print('Recived in microservice')
    data = json.loads(body)
    print(data)

    if properties.content_type == 'page_created':
        page = {
            'page': data['id'],
            'counters': {
                'count_follower': data['followers'],
                'count_follow_requests':  data['follow_requests']
            }
        }
        db_manager.add_counter(page)
    
    elif properties.content_type == 'page_updated':
        page = data['id']
        count_follower = data['followers']
        count_follow_requests = data['follow_requests']
        db_manager.update_counter(page, count_follow_requests, count_follower)

    elif properties.content_type == 'page_deleted':
        page = data['id'],
        db_manager.delete_counter(page)

channel.basic_consume(queue='microservice', on_message_callback=callback, auto_ack=True)

print('Started consuming')

channel.start_consuming()

channel.close()