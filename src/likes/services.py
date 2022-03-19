from .models import Like
from users.models import User
from posts.models import Post
from django.db.models import F


def add_like(obj, user):
    """Liked the `obj`.
    """
    if not Like.objects.filter(user=user, post=obj):
        Like.objects.create(user=user, post=obj)
        Post.objects.filter(pk=obj.id).update(total_likes=F('total_likes')+1)


def remove_like(obj, user):
    """Removed 'like' the `obj`.
    """
    if Like.objects.filter(user=user, post=obj):
        Like.objects.filter(user=user, post=obj).delete()
        Post.objects.filter(pk=obj.id).update(total_likes=F('total_likes')-1)


def is_fan(obj, user):
    """Check user's like the `obj`.
    """
    if not user.is_authenticated:
        return False
    likes = Like.objects.filter(user=user, post=obj)
    return likes.exists()


def get_fans(obj):
    """Get a list of users who liked `obj`.
    """
    return User.objects.filter(likes__post=obj)
