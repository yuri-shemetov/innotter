from .views import PageModelViewSet
from rest_framework.routers import DefaultRouter


app_name = 'pages'
# Create router and Registration ViewSet
router = DefaultRouter()
router.register(r'', PageModelViewSet, basename='pages')
# URLs
urlpatterns = router.urls
