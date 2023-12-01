from django.urls import path
from django.contrib.auth import views as auth_views

from .views import logout_view, RegistrationView

app_name = 'users'

urlpatterns = [
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='login.html'),
        name='login',
    ),
    path('logout/', logout_view, name='logout'),
    path('register/', RegistrationView.as_view(), name='register'),
]
