from .views import posts, index
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('posts/', posts, name='posts')
]