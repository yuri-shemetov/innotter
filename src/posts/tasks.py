from __future__ import absolute_import, unicode_literals
from django.core.mail import send_mass_mail
from proj.celery import app


@app.task
def send_new_post_email(users_email, name_page):
    send_mass_mail(
        'New post for the page.',
        f'The post have been create for the page "{name_page}".',
        'yuri7shemetov@gmail.com',
        users_email,
        fail_silently=False
    )
