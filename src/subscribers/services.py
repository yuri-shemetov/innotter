from .models import Subscriber
from pages.models import Page
from users.models import User


def add_subscription(obj, user):
    """Added the `obj`.
    """
    if user.is_staff:
        subscription, is_created = Subscriber.objects.get_or_create(
            subscriber=user, follower=obj)
        return subscription
    elif user.is_authenticated and Page.objects.filter(id=obj.id, is_private=False):
        subscription, is_created = Subscriber.objects.get_or_create(
            subscriber=user, follower=obj)
        return subscription
    elif user.is_authenticated and Page.objects.filter(id=obj.id, is_private=True):
        subscription, is_created = Subscriber.objects.get_or_create(
            subscriber=user, follow_requests=obj)
        return subscription


def confirm_subscription_everybody(obj, user):
    if user.is_authenticated and Page.objects.filter(id=obj.id, owner=user):
        follow_requests = User.objects.filter(subscribers__follow_requests=obj)
        for everybody in follow_requests:
            subscription, is_created = Subscriber.objects.get_or_create(
                subscriber=everybody, follower=obj)
            Subscriber.objects.filter(
                subscriber=everybody, follow_requests=obj).delete()
            return subscription


def remove_subscription(obj, user):
    """Removed 'subscription' on the `obj`.
    """
    if user.is_authenticated and Page.objects.filter(id=obj.id, owner=user):
        Subscriber.objects.filter(follower=obj).delete()
    elif user.is_authenticated:
        Subscriber.objects.filter(subscriber=user, follower=obj).delete()


def get_follow_requests(obj):
    """Get a list of users who requested subscribtion on the `obj`.
    """
    return User.objects.filter(subscribers__follow_requests=obj)


def get_subscribers(obj):
    """Get a list of users who subscribed on the `obj`.
    """
    return User.objects.filter(subscribers__follower=obj)


def get_count_follow_requests(obj):
    """Get a count of users who requested subscribtion on the `obj`.
    """
    return User.objects.filter(subscribers__follow_requests=obj).count()


def get_count_subscribers(obj):
    """Get a count of users who subscribed on the `obj`.
    """
    return User.objects.filter(subscribers__follower=obj).count()


def is_subscriber(obj, user):
    """Check user is subscriber on the `obj`.
    """
    if not user.is_authenticated:
        return False
    subscriber = Subscriber.objects.filter(subscriber=user, follower=obj)
    return subscriber.exists()


def is_follow_requests(obj, user):
    """Check user is follow_requests on the `obj`.
    """
    if not user.is_authenticated:
        return False
    subscriber = Subscriber.objects.filter(
        subscriber=user, follow_requests=obj)
    return subscriber.exists()
