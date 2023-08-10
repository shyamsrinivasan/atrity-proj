from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import SignupView

# app_name = 'userapp'
urlpatterns = [path('sign-up/', SignupView.as_view(), name='user-sign-up'),
               path('login/',
                    auth_views.LoginView.as_view(template_name='userapp/registration/login.html'),
                    name='user-login')
               ]

