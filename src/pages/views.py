from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import PageSerializer
from .models import Page
from django.db.models import Q


class PageModelViewSet(viewsets.ModelViewSet):
    """Allowed Pages for everybody categories"""
    serializer_class = PageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Page.objects.all()

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Page.objects.all()
        elif user.is_authenticated:
            return Page.objects.filter(
                Q(owner=user) | Q(is_private=False)
            ).order_by('-updated_at')
        else:
            return Page.objects.filter(is_private=False)
