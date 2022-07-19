import pika
import json
from api import db_manager, local_settings

params = pika.URLParameters(local_settings.BROKER_URL_FOR_DB)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='microservice')


def callback(ch, method, properties, body):
    print('Recived in microservice')
    data = json.loads(body)
    print(data)
    if properties.content_type == 'page_created':
        page = data['id']
        count_follower = data['count_followers']
        count_follow_requests = data['count_follow_requests']
        db_manager.add_counter(page, count_follow_requests, count_follower)

    elif properties.content_type == 'page_updated':
        page = data['id']
        count_follower = data['count_followers']
        count_follow_requests = data['count_follow_requests']
        db_manager.update_counter(page, count_follow_requests, count_follower)

    elif properties.content_type == 'page_deleted':
        db_manager.delete_counter(data)

    elif properties.content_type == 'page_subscribed':
        db_manager.increase_count_followers(data)

    elif properties.content_type == 'page_request_subscribed':
        db_manager.increase_count_follow_requests(data)

    elif properties.content_type == 'page_confirm':
        db_manager.decrease_increase(data)

    elif properties.content_type == 'page_unconfirm':
        db_manager.decrease_count_follow_requests(data)

    elif properties.content_type == 'page_delete_subscribers':
        db_manager.delete_followers(data)

    elif properties.content_type == 'decrease_count_followers':
        db_manager.decrease_count_follower(data)


channel.basic_consume(
    queue='microservice',
    on_message_callback=callback,
    auto_ack=True
    )

print('Started consuming')

channel.start_consuming()

channel.close()
