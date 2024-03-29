from .models import Subscriber
from pages.models import Page
from users.models import User
from producer import publish


def add_subscription(obj, user):
    """Added the `obj`.
    """
    if user.is_staff:
        subscription, is_created = Subscriber.objects.get_or_create(
            subscriber=user, follower=obj)
        if is_created:
            publish('page_subscribed', str(obj.id))
        return subscription
    elif user.is_authenticated and Page.objects.filter(id=obj.id, is_private=False):
        subscription, is_created = Subscriber.objects.get_or_create(
            subscriber=user, follower=obj)
        if is_created:
            publish('page_subscribed', str(obj.id))
        return subscription
    elif user.is_authenticated and Page.objects.filter(id=obj.id, is_private=True):
        subscription, is_created = Subscriber.objects.get_or_create(
            subscriber=user, follow_requests=obj)
        if is_created:
            publish('page_request_subscribed', str(obj.id))
        return subscription


def confirm_subscription_everybody(obj, user):
    if user.is_authenticated and Page.objects.filter(owner=user).exists():
        follow_requests = User.objects.filter(subscribers__follow_requests=obj)
        for one_user in follow_requests:
            subscription = Subscriber.objects.filter(subscriber=one_user).update(follower=obj, follow_requests=None)
            publish('page_subscribed', str(obj.id))
            return subscription


def remove_subscription(obj, user):
    """Removed 'subscription' on the `obj`.
    """
    if user.is_authenticated and Page.objects.filter(id=obj.id, owner=user).exists():
        Subscriber.objects.filter(follower=obj).delete()
        publish('page_delete_subscribers', str(obj.id))
    elif user.is_authenticated:
        if Subscriber.objects.filter(subscriber=user, follower=obj).exists():
            Subscriber.objects.filter(subscriber=user, follower=obj).delete()
            publish('decrease_count_followers', str(obj.id))


def get_follow_requests(obj):
    """Get a list of users who requested subscribtion on the `obj`.
    """
    return User.objects.filter(subscribers__follow_requests=obj)


def get_subscribers(obj):
    """Get a list of users who subscribed on the `obj`.
    """
    return User.objects.filter(subscribers__follower=obj)


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
