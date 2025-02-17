from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse
from django.template.loader import render_to_string

menu = [{'title':'about site', 'url_name':'about_name'}, 
        {'title':'add page', 'url_name':'add_name'}, 
        {'title':'contacts', 'url_name':'contacts_name'}, 
        {'title':'sign in', 'url_name':'sign_name'}]
def index_http(request:HttpRequest):
    #index_html = render_to_string('main/index.html')
    #return HttpResponse(index_html)
    data = {
        'title': 'home',
        'list':menu,
        'ist':[
            {'name':'steve', 'age':22, 'description':'do his work quick'}, 
            {'name':'jim', 'age':33, 'description':'do his work well'}, 
            ]
        }
    try:
        return render(request, 'main/index.html', data)
    except(Exception) as err:
        print(err)

def about(request:HttpRequest):
    data = {
        'title':'about us',
        'content_1':'our company provide service with installing and deinstalling electrecian equipment.',
        'content_2':'also we can provide other services like cleaning and installing plumbing.',
        'content_3':'', 
        }
    return render(request, 'main/about.html', data)


def add(request:HttpRequest):
    data = {
        'content_1':'new page adding.',
        'content_2':'',
        'content_3':'', 
        }
    return render(request, 'main/add.html', data)

def contacts(request:HttpRequest):
    data = {
        'content_1':'call us if you face with some problems associated with our services.',
        'content_2':['+110-444-222-4', '+555-222-454'],
        'content_3':'',
        }
    return render(request, 'main/contacts.html', data)

def sign(request:HttpRequest):
    data = {
        'content_1':'sign up',
        'content_2':'',
        'content_3':'',
        }
    return render(request, 'main/sign.html', data)


def page_not_found(request:HttpRequest, exception):
    return HttpResponseNotFound('<h2>Page not found, asshole</h2>')


    