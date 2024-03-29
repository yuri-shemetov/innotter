from django.db import models
import uuid


class Page(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    owner = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='pages'
    )
    name = models.CharField(
        max_length=80
    )
    description = models.TextField()
    tag = models.ForeignKey(
        'tags.Tag',
        on_delete=models.CASCADE,
        related_name='tags'
    )
    image = models.FileField(
        max_length=30,
        null=True,
        blank=True
    )
    is_private = models.BooleanField(
        default=False
    )
    count_followers = models.IntegerField(default=0)
    count_follow_requests = models.IntegerField(default=0)
    unblock_date = models.DateTimeField(
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
    )
