from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def index_http(request:HttpRequest):
    return HttpResponse('<h2>Главная страница</h2>')
def categories(request:HttpRequest):
    return HttpResponse('<h1>Категории</h1>')

    