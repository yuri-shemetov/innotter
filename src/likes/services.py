from .models import Like
from users.models import User


def add_like(obj, user):
    """Liked the `obj`.
    """

    like, is_created = Like.objects.get_or_create(
        user=user, post=obj)
    return like

def remove_like(obj, user):
    """Removed 'like' the `obj`.
    """

    Like.objects.filter(
        user=user, post=obj
    ).delete()

def is_fan(obj, user):
    """Check user's like the `obj`.
    """

    if not user.is_authenticated:
        return False

    likes = Like.objects.filter(
        user=user, post=obj)
    return likes.exists()
    
def get_fans(obj):
    """Get a list of users who liked `obj`.
    """
    return User.objects.filter(likes__post=obj)

def get_count_fans(obj):
    """Get a count of users who liked `obj`.
    """
    return User.objects.filter(likes__post=obj).count()