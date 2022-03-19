from django.db import models


class Post(models.Model):
<<<<<<< HEAD
    page = models.ForeignKey(
       'pages.Page',
       on_delete=models.CASCADE,
       related_name='posts'
    )
    content = models.CharField(max_length=180)
    reply_to = models.ForeignKey(
       'posts.Post',
       on_delete=models.SET_NULL,
       null=True,
       blank=True,
       related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
=======
   page = models.ForeignKey(
      'pages.Page',
      on_delete=models.CASCADE,
      related_name='posts'
   )
   content = models.CharField(max_length=180)
   reply_to = models.ForeignKey(
      'posts.Post',
      on_delete=models.SET_NULL,
      null=True,
      blank=True,
      related_name='replies'
   )
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)
   total_likes = models.IntegerField(default=0)
>>>>>>> 6b5f6e454b4fa8840fd8da4e8da5ad329506f2eb
