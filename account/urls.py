from django.contrib.auth.views import LoginView, LogoutView
from .views import register, profile
from django.urls import include, path

app_name = 'account'

urlpatterns = [
    path('login/', LoginView.as_view(
            template_name='registration/login.html',
            next_page='account:profile'
        ), name='login'
    ),
    path('logout/', LogoutView.as_view(
            template_name='registration/login.html',
            next_page='index'
        ), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('', include('django.contrib.auth.urls'))
]