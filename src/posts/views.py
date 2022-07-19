from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import PostSerializer
from .models import Post
from pages.models import Page
from likes.models import Like
from subscribers.models import Subscriber
from likes.mixins import LikedMixin
from .tasks import send_new_post_email
from rest_framework.response import Response
from rest_framework import status


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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        # send the list emails
        page = serializer.validated_data['page']
        if request.user.is_authenticated:
            subscribers = Subscriber.objects.filter(follower=page)
            users_email = list(map(lambda n: n.subscriber.email, subscribers))
            send_new_post_email.delay(users_email, page.name)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PostLikeModelViewSet(viewsets.ModelViewSet):
    """Allowed to see Posts that liked"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        like_posts = Like.objects.filter(user=user)
        return Post.objects.filter(like_post__in=like_posts)
