from django.db import models
from users.models import User


class Like(models.Model):
    user = models.ForeignKey(
        User,
        related_name='likes',
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        'posts.Post',
        related_name='like_post',
        on_delete=models.CASCADE
    )
