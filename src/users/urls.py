from django.urls import path
from .views import RegistrationAPIView, LoginAPIView, UserRetrieveUpdateAPIView, UserList, UserDetail

app_name = 'auth'
urlpatterns = [
    path('user-update/', UserRetrieveUpdateAPIView.as_view()),
    path('registration/', RegistrationAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]