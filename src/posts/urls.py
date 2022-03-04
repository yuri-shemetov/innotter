from .views import PostModelViewSet
from rest_framework.routers import DefaultRouter


app_name = 'posts'
# Create router and Registration ViewSet
router = DefaultRouter()
router.register(r'', PostModelViewSet, basename='posts')
# URLs
urlpatterns = router.urls
