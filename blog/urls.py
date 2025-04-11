from .views import post_list, post_details
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post_slug>', post_details, name='post_details')
]