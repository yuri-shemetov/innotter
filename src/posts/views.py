from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import PostSerializer
from .models import Post
from pages.models import Page
from likes.mixins import LikedMixin
from django.db.models import Q


class PostModelViewSet(LikedMixin, viewsets.ModelViewSet):
    "Posts"
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Post.objects.all()
        elif user.is_authenticated:
            permissions_pages = [i for i in Page.objects.filter(Q(owner=user)|Q(is_private=False))]
            return Post.objects.filter(page__in=permissions_pages)
        else:
            permissions_pages = [i for i in Page.objects.filter(is_private=False)]
            return Post.objects.filter(page__in=permissions_pages)
