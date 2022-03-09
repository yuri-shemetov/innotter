from django.urls import path, include


app_name = 'api'
urlpatterns = [
    path('users/', include('users.urls', namespace='auth')),
    path('pages/', include('pages.urls', namespace='pages')),
    path('posts/', include('posts.urls', namespace='posts')),
    path('subscribers/', include('subscribers.urls', namespace='subscribers')),
]
