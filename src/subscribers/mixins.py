from rest_framework.decorators import action
from rest_framework.response import Response
from . import services
from .serializers import SubscriberUserSerializer


class SubscribersMixin:
    @action(detail=True, methods=['POST'])
    def subscribes(self, request, pk=None):
        """Subscribes to `obj`.
        """
        obj = self.get_object()
        services.add_subscription(obj, request.user)
        return Response()

    @action(detail=True, methods=['POST'])
    def unsubscribes(self, request, pk=None):
        """Remove 'subscribers' from `obj`.
        """
        obj = self.get_object()
        services.remove_subscription(obj, request.user)
        return Response()

    @action(detail=True, methods=['GET'])
    def follow_requests(self, request, pk=None):
        """Get a list of users who requested subscribtion on the `obj`.
        """
        obj = self.get_object()
        follow_requests = services.get_follow_requests(obj)
        serializer = SubscriberUserSerializer(follow_requests, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def followers(self, request, pk=None):
        """Get a list of users who subscribed on the `obj`.
        """
        obj = self.get_object()
        subscribers = services.get_subscribers(obj)
        serializer = SubscriberUserSerializer(subscribers, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['POST'])
    def confirm(self, request, pk=None):
        """Confirm for everybody to `obj`.
        """
        obj = self.get_object()
        services.confirm_subscription_everybody(obj, request.user)
        return Response()
