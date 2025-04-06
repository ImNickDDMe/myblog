from .views import post_list, post_details
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', post_list, name='post_list'),
    path('<int:post_id>/', post_details, name='post_details')
]