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
        on_delete=models.CASCADE
    )
