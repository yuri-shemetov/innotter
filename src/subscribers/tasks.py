from __future__ import absolute_import, unicode_literals
from django.core.mail import send_mail
from proj.celery import app


@app.task
def send_letter_email(user_mail, name_page):
    send_mail(
        'Congratulations! You have subscribed to the newsletter!',
        f'Now you will receive all new post`s the page "{name_page}".',
        'yuri7shemetov@gmail.com',
        [user_mail],
        fail_silently=False,
    )
