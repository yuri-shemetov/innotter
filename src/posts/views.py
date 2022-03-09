from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import PostSerializer
from .models import Post
from pages.models import Page
from subscribers.models import Subscriber
from likes.mixins import LikedMixin
from django.db.models import Q


class PostModelViewSet(LikedMixin, viewsets.ModelViewSet):
    """Allowed Posts for everybody categories"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Post.objects.all()
        elif user.is_authenticated:
            permissions_pages = [
                i for i in Page.objects.all() if Subscriber.objects.filter(
                    Q(subscriber=user) & Q(follower=i)
                )
            ]
            return Post.objects.filter(page__in=permissions_pages)
