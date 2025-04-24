from .views import PostListView, post_details, post_share, post_comment
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(template_name='post/post_list.html'), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post_slug>', post_details, name='post_details'),
    path('share/<slug:post_slug>', post_share, name='post_share'),
    path('comment/<slug:post_slug>', post_comment, name='post_comment')
]