from .views import post_list, post_details, post_share, post_comment
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post_slug>', post_details, name='post_details'),
    path('share', post_share, name='post_share'),
    path('comment/<int:id>', post_comment, name='post_comment')
]