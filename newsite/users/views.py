from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from .forms import LoginUserForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
# Create your views here.
def login_user(request:HttpRequest):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, 
                username=cd['username'],
                password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home_name'))
    else:
        form = LoginUserForm()


    return render(request, 'users/login.html', {'form':form,})

def logout_user(request:HttpRequest):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))