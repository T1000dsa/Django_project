from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from .forms import LoginUserForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

class UserLogin(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {
        'title':'Autorization'
    }
    #def get_success_url(self):
    #   return reverse_lazy('home_name')

class LogoutUser(LogoutView):pass