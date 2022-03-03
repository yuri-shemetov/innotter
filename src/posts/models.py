from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from likes.models import Like


class Post(models.Model):
    page = models.ForeignKey(
       'pages.Page',
        on_delete=models.CASCADE, 
        related_name='posts'
    )
    content = models.CharField(max_length=180)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = GenericRelation(Like)
    @property
    def total_likes(self):
        return self.likes.count()