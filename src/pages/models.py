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
        related_name='pages'
    )
    image = models.URLField(
        null=True, 
        blank=True
    )
    is_private = models.BooleanField(
        default=False
    )
    followers = models.ManyToManyField(
        'users.User', 
        related_name='follows'
    )
    follow_requests = models.ManyToManyField(
        'users.User', 
        related_name='requests'
    )
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