from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from .serializers import PostSerializer
from .models import Post
from pages.models import Page
class PostModelViewSet(viewsets.ModelViewSet):
    "Posts"
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Post.objects.all()
        elif user.is_authenticated:
            page = Page.objects.filter(owner=user)
            post_for_me=[]
            for i in page:
                post_for_me += Post.objects.filter(page=i)
            return post_for_me
