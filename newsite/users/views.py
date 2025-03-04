from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from .forms import LoginUserForm, RegisterUserForm, ProfileUserForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
# Create your views here.

class UserLogin(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {
        'title':'Autorization'
    }

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    extra_context = {
        'title':'Registration'
    }


class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'users/profile.html'
    extra_context = {
        'title':'Profile'
    }

    def get_success_url(self):
        return reverse_lazy('users:profile')
    def get_object(self, queryset = None):
        return self.request.user

class LogoutUser(LogoutView):pass