from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import PostSerializer
from .models import Post
from pages.models import Page
from likes.models import Like
from subscribers.models import Subscriber
from likes.mixins import LikedMixin


class PostModelViewSet(LikedMixin, viewsets.ModelViewSet):
    """Allowed to Posts for for concrete categories"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Post.objects.all().order_by('-updated_at')
        elif user.is_authenticated:
            owner_pages = Page.objects.filter(owner=user)
            subscriber_user = Subscriber.objects.filter(subscriber=user)
            permissions_pages = Page.objects.filter(
                followers__in=subscriber_user)
            return Post.objects.filter(
                page__in=permissions_pages | owner_pages
            ).order_by('-updated_at')


class PostLikeModelViewSet(viewsets.ModelViewSet):
    """Allowed to see Posts that liked"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        like_posts = Like.objects.filter(user=user)
        return Post.objects.filter(like_post__in=like_posts)
