from rest_framework import viewsets, filters, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import PageSerializer
from .models import Page
from subscribers.mixins import SubscribersMixin
from users.models import User
from rest_framework.response import Response
from subscribers.producer import follower


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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        follower('page_created', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        follower('page_updated', serializer.data)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        instance = self.get_object()
        follower('page_deleted', pk)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
