from .views import register, profile, CustomLoginView
from django.urls import include, path

app_name = 'account'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('', include('django.contrib.auth.urls'))
]