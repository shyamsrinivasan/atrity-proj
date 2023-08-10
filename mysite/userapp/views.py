from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponseRedirect, JsonResponse

from .forms import NewUserForm


# Create your views here.
class SignupView(generic.CreateView):
    """view class for user sign up"""
    form_class = NewUserForm
    success_url = reverse_lazy('user-login')
    template_name = 'userapp/registration/signup.html'

    def __init__(self, *args, **kwargs):
        super(SignupView, self).__init__(*args, **kwargs)

    def form_valid(self, form):
        """overrides parent class method"""
        # call super to execute parent class method
        self.object = form.save(commit=False)
        self.object.save()
        # response = super(SignupView, self).form_valid(form)
        # if self.request.accepts("text/html"):
        #     return response
        # else:
        #     return JsonResponse({'pk': self.object.pk})
        return HttpResponseRedirect(self.get_success_url())

