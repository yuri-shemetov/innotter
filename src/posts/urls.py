from .views import PostModelViewSet, PostLikeModelViewSet
from rest_framework.routers import DefaultRouter


app_name = 'posts'
# Create router and Registration ViewSet
router = DefaultRouter()
router.register(r'posts', PostModelViewSet, basename='posts')
router.register(r'likes', PostLikeModelViewSet, basename='likes')
# URLs
urlpatterns = router.urls
