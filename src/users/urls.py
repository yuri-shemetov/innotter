from django.urls import path
from .views import (
    RegistrationAPIView, LoginAPIView, UserUpdateAPIView, UserModelViewSet
)
from rest_framework.routers import DefaultRouter


app_name = 'auth'
# Create router and Registration ViewSet
router = DefaultRouter()
router.register(r'', UserModelViewSet, basename='users')
# For user authentication
urlpatterns = [
    path('registration/', RegistrationAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('user-update/', UserUpdateAPIView.as_view()),
]
# URLs
urlpatterns += router.urls
