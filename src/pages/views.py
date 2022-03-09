from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import PageSerializer
from .models import Page
from subscribers.mixins import SubscribersMixin


class PageModelViewSet(SubscribersMixin, viewsets.ModelViewSet):
    """Allowed Pages for everybody categories"""
    serializer_class = PageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Page.objects.all()
