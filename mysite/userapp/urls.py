from django.urls import path

from .views import SignupView

# app_name = 'userapp'
urlpatterns = [path('sign-up/', SignupView.as_view(), name='user-sign-up'),
               ]
