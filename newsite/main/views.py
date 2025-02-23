from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse
from django.template.loader import render_to_string
from main.models import Worker, Category, TagModel
from main.forms import AddPostForm, UploadClassForm
from datetime import datetime

menu = [{'title':'about site', 'url_name':'about_name'}, 
        {'title':'add page', 'url_name':'add_name'}, 
        {'title':'contacts', 'url_name':'contacts_name'}, 
        {'title':'sign in', 'url_name':'sign_name'}]
def index_http(request:HttpRequest):
    posts = Worker.published.all().exclude(slug='').select_related('cat')
    data = {
        'title':'home',
        'menu':menu,
        'post':posts,
        'cat_selected':0,
        }
    try:
        return render(request, 'main/index.html', data)
    except(Exception) as err:
        print(err, index_http)

def handle_uploaded_file(f):
    timemark = datetime.now().timestamp()
    with open(f"newsite/uploads/{timemark}_{f.name}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def about(request:HttpRequest):
    if request.method == 'POST':
        form = UploadClassForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(form.cleaned_data['file'])

    else:
        form = UploadClassForm()
    data = {
        'title':'about us',
        'content_1':'our company provide service with installing and deinstalling electrecian equipment.',
        'content_2':'also we can provide other services like cleaning and installing plumbing.',
        'form':form
        }
    return render(request, 'main/about.html', data)


def add(request:HttpRequest):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            #print(form.cleaned_data)
            #try:
            #    Worker.objects.create(**form.cleaned_data)
            #    return redirect('home_name')
            #except Exception as err:
            #    print(err)
            #    form.add_error(None, 'Error with adding new data!')
            form.save()
            return redirect('home_name')

    else:
        form = AddPostForm()
    data = {
            'title':'adding',
            'content_1':'new page adding.',
            'form':form
            }
    return render(request, 'main/add.html', data)


def contacts(request:HttpRequest):
    data = {
        'title':'contacts',
        'content_1':'call us if you face with some problems associated with our services.',
        'content_2':['+110-444-222-4', '+555-222-454'],
        'content_3':'',
        }
    return render(request, 'main/contacts.html', data)


def sign(request:HttpRequest):
    data = {
        'title':'sign up/sigh in',
        'content_1':'sign up',
        'content_2':'',
        'content_3':'',
        }
    return render(request, 'main/sign.html', data)


def show_cat(request:HttpRequest, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Worker.objects.filter(cat_id=category.pk).select_related('cat')
    data = {
        'title': f'Category: {category.name}',
        'list':menu,
        'post':posts,
        'cat_selected':category.pk
        }
    return render(request, 'main/includes/selected.html', data)


def show_post(request:HttpRequest, post_slug):
    db_data = get_object_or_404(Worker, slug=post_slug)
    data = {
        'title': 'Show Post',
        'list':menu,
        'post':db_data,
        'cat_selected':0
        }
    try:
        return render(request, 'main/post.html', data)
    except(Exception) as err:
        print(err, show_tag_postlist)


def show_tag_postlist(request:HttpRequest, tag_slug):
    tag = get_object_or_404(TagModel, slug=tag_slug)
    posts = tag.tags.filter(is_published=Worker.Status.Published)
    data = {
        'title':f'Tag: {tag.tag}',
        'menu':menu,
        'post':posts,
        'cat_selected':None,
        'tags_bool':1
    }
    try:
        return render(request,'main/index.html',  data)
    except(Exception) as err:
        print(err, show_tag_postlist)

def page_not_found(request:HttpRequest, exception):
    return render(request, 'main/not_found.html')
    