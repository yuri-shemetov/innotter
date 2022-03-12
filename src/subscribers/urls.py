from .views import SubscriberModelViewSet
from rest_framework.routers import DefaultRouter


app_name = 'subscribers'
# Create router and Registration ViewSet
router = DefaultRouter()
router.register(r'', SubscriberModelViewSet, basename='subscribers')
# URLs
urlpatterns = router.urls
