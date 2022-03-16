from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import PageSerializer
from .models import Page
from subscribers.mixins import SubscribersMixin
from users.models import User
from rest_framework.response import Response


class PageModelViewSet(SubscribersMixin, viewsets.ModelViewSet):
    """Allowed Pages for everybody categories"""
    serializer_class = PageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Page.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'id', 'tag__name']

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Page.objects.all().order_by('-updated_at')
        else:
            users = User.objects.filter(is_active=True)
            return Page.objects.filter(owner__in=users).order_by('-updated_at')
