from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

class Tag(models.Model):
    owner = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='tags'
    )
    name = models.CharField(
        max_length=30, 
        unique=True
    )
    content_type = models.ForeignKey(
        ContentType, 
        on_delete=models.CASCADE
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey(
        'content_type', 
        'object_id'
    )