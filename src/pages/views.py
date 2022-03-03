from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from .serializers import PageSerializer
from .models import Page

# from posts.mixins import PostMixin

class PageModelViewSet(viewsets.ModelViewSet):
    "Pages"
    serializer_class = PageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Page.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Page.objects.all()
        elif user.is_authenticated:
            return Page.objects.filter(owner=user)
