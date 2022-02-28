from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from tags.models import Tag

class Page(models.Model):
    owner = models.ForeignKey(
        'users.User', 
        on_delete=models.CASCADE, 
        related_name='pages'
    )
    name = models.CharField(
        max_length=80
    )
    uuid = models.CharField(
        max_length=30, 
        unique=True
    )
    description = models.TextField()
    tags = GenericRelation(Tag)
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
