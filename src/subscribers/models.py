from django.db import models
from users.models import User


class Subscriber(models.Model):
    subscriber = models.ForeignKey(
        User,
        related_name='subscribers',
        on_delete=models.CASCADE
    )
    follower = models.ForeignKey(
        'pages.Page',
        related_name='followers',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    follow_requests = models.ForeignKey(
        'pages.Page',
        related_name='follow_requests',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
