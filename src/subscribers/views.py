from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import SubscriberSerializer
from .models import Subscriber
from django.db.models import Q
from rest_framework.decorators import action
from users.models import User
from pages.models import Page
from rest_framework.response import Response
from . tasks import send_letter_email


class SubscriberModelViewSet(viewsets.ModelViewSet):
    """Subscribers"""
    serializer_class = SubscriberSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Subscriber.objects.all()

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Subscriber.objects.all()
        elif user.is_authenticated:
            pages = Page.objects.filter(owner=user)
            for page in pages:
                return Subscriber.objects.filter(
                    Q(follower=page) | Q(follow_requests=page)
                )

    @action(detail=True, methods=['POST'])
    def confirm(self, request, pk=None):
        """Confirm for one user to `obj`.
        """
        subscribers = self.get_object()
        if request.user.is_authenticated and Page.objects.filter(owner=request.user):
            one_user = User.objects.get(pk=subscribers.subscriber.id)
            subscription, is_created = Subscriber.objects.get_or_create(
                subscriber=one_user, follower=subscribers.follow_requests)
            send_letter_email.delay(subscribers.subscriber.email, subscribers.follow_requests.name) # CELERY
            Subscriber.objects.filter(
                subscriber=one_user,
                follow_requests=subscribers.follow_requests
            ).delete()
        return Response()

    @action(detail=True, methods=['POST'])
    def unconfirm(self, request, pk=None):
        """Unconfirm for one user to `obj`.
        """
        subscribers = self.get_object()
        if request.user.is_authenticated and Page.objects.filter(owner=request.user):
            one_user = User.objects.get(pk=subscribers.subscriber.id)
            Subscriber.objects.filter(
                subscriber=one_user,
                follow_requests=subscribers.follow_requests
            ).delete()
        return Response()
