from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


# Create your views here.
class SignupView(generic.CreateView):
    """view class for user sign up"""
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'userapp/registration/signup.html'
