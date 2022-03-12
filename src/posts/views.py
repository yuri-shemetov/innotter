from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import PostSerializer
from .models import Post
from pages.models import Page
from likes.models import Like
from subscribers.models import Subscriber
from likes.mixins import LikedMixin
from django.db.models import Q


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
            permissions_pages = [
                i for i in Page.objects.all() if Subscriber.objects.filter(
                    Q(subscriber=user) & Q(follower=i)
                )
            ]
            return Post.objects.filter(
                Q(page__in=permissions_pages) | Q(page__in=owner_pages)
            ).order_by('-updated_at')


class PostLikeModelViewSet(viewsets.ModelViewSet):
    """Allowed to see Posts that liked"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        like_posts = [
            i.pk for i in Post.objects.all() if Like.objects.filter(
                Q(user=user) & Q(post=i)
            )
        ]
        return Post.objects.filter(pk__in=like_posts)
