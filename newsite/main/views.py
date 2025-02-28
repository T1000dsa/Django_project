from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse, reverse_lazy
from django.template.loader import render_to_string
from main.models import Worker, Category, TagModel, UploadFiles
from main.forms import AddPostForm, UploadClassForm
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from .utils import DataMixin
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexHome(DataMixin, ListView):
    model = Worker
    template_name = 'main/index.html'
    title_page = 'home'

    def get_queryset(self):
        return Worker.published.all()
    
    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        return self.get_mixin_context(contex,
                                      index_list=contex['worker_list'])

def about(request:HttpRequest):
    data = {
        'title':'about us',
        'content_1':'our company provide service with installing and deinstalling electrecian equipment.',
        'content_2':'also we can provide other services like cleaning and installing plumbing.',

        }
    return render(request, 'main/about.html', data)

class About(DataMixin, FormView):
    data = {
        'title':'about us',
        'content_1':'our company provide service with installing and deinstalling electrecian equipment.',
        'content_2':'also we can provide other services like cleaning and installing plumbing.',
        }
    template_name = 'main/about.html'
    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        return self.get_mixin_context(
            contex,
            **self.data
            )
    def query_set(self, request):
        return request


class AddPage(LoginRequiredMixin, CreateView):
    form_class = AddPostForm
    template_name = 'main/add.html'
    success_url = reverse_lazy('home_name')

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['title'] = 'adding'
        return contex

   
    
class UpdatePage(LoginRequiredMixin, DataMixin, UpdateView):
    model = Worker
    fields = "__all__" # ['title', 'slug', 'content', 'photo', 'is_published', 'cat', 'helmet']
    template_name = 'main/add.html'
    success_url = reverse_lazy('home_name')
    title_page = 'editing'


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
        }
    return render(request, 'main/sign.html', data)


class Show_cat(LoginRequiredMixin, DataMixin, ListView):
    model = Category
    template_name = 'main/selected.html'
    context_object_name = 'post'
    allow_empty = False

    def get_queryset(self):
        return Worker.published.filter(cat__slug=self.kwargs['cat_slug']).exclude(slug='').select_related('cat')
    
    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        cat = contex['post'][0].cat
        return self.get_mixin_context(
            contex, 
            title=f'Category: {cat.name}',
            cat_selectet = cat.pk
            )
    

class Show_Post(LoginRequiredMixin, DataMixin, DetailView):
    model = Worker
    template_name = 'main/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'
    

    def get_object(self, queryset=None):
        return get_list_or_404(Worker.published, slug=self.kwargs[self.slug_url_kwarg])[0]
    
    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        return self.get_mixin_context(contex, 
                                      title=contex['object'].title,
                                      post=contex['object'])
    
class Show_tag(LoginRequiredMixin, DataMixin, ListView):
    model = TagModel
    template_name = 'main/index.html'

    def get_queryset(self):
        data = Worker.published.filter(tags__slug=self.kwargs['tag_slug'])
        return data
    
    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        tag = contex['view'].kwargs
        return self.get_mixin_context(
            contex, 
            title=f'tag: {tag['tag_slug']}',
            post=contex['worker_list'])
    

class DeletePost(LoginRequiredMixin, DataMixin, DeleteView):
    model = Worker
    template_name = 'main/delete_page.html'
    context_object_name = 'post'
    success_url = reverse_lazy('home_name')
    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        return self.get_mixin_context(
            contex, 
            title='delete', 
            )

def page_not_found(request:HttpRequest, exception):
    return render(request, 'main/not_found.html')