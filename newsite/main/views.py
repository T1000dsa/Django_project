from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse
from django.template.loader import render_to_string
from main.models import Worker, Category, TagModel, UploadFiles
from main.forms import AddPostForm, UploadClassForm
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
menu = [{'title':'about site', 'url_name':'about_name'}, 
        {'title':'add page', 'url_name':'add_name'}, 
        {'title':'contacts', 'url_name':'contacts_name'}, 
        {'title':'sign in', 'url_name':'sign_name'}]

class IndexHome(ListView):
    model = Worker
    template_name = 'main/index.html'
    #context_object_name = 'post'
    posts = Worker.published.all().exclude(slug='').select_related('cat')
    template_name = 'main/index.html'
    extra_context = {
        'title':'home',
        'menu':menu,
        'post':posts,
        'cat_selected':0,
    }
    def get_queryset(self):
        return Worker.published.all().exclude(slug='').select_related('cat')

    #def get_context_data(self, **kwargs):
        #contex = super().get_context_data(**kwargs)
        #contex['title'] = 'title'
        #contex['cat_selected'] = int(self.request.GET.get('cat_id', 0))
        #return contex

#def handle_uploaded_file(f):
#    timemark = datetime.now().timestamp() 
#    with open(f"newsite/uploads/{timemark}_{f.name}", "wb+") as destination:
#       for chunk in f.chunks():
#           destination.write(chunk)

def about(request:HttpRequest):
    if request.method == 'POST':
        form = UploadClassForm(request.POST, request.FILES)
        if form.is_valid():
            fp = UploadFiles(file=form.cleaned_data['file'])
            fp.save()

    else:
        form = UploadClassForm()
    data = {
        'title':'about us',
        'content_1':'our company provide service with installing and deinstalling electrecian equipment.',
        'content_2':'also we can provide other services like cleaning and installing plumbing.',
        'form':form
        }
    return render(request, 'main/about.html', data)



class AddPage(View):
    data = {
            'title':'adding',
            'content_1':'new page adding.',
            'form':None
            }
    
    def get(self, request:HttpRequest):
        self.data['form'] = AddPostForm()
        return render(request, 'main/add.html', self.data)
    def post(self, request:HttpRequest):
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            self.data['form'] = form

        return redirect('home_name')


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


class Show_cat(ListView):
    model = Category
    template_name = 'main/includes/selected.html'
    context_object_name = 'post'
    allow_empty = False
    def get_queryset(self):
        return Worker.published.filter(cat__slug=self.kwargs['cat_slug']).exclude(slug='').select_related('cat')
    
    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        cat = contex['post'][0].cat
        contex['title'] = f'Category: {cat.name}'
        contex['cat_selected'] = cat.pk
        return contex


def show_post(request:HttpRequest, post_slug):
    db_data = get_object_or_404(Worker, slug=post_slug)
    print(db_data.photo.url)
    data = {
        'title': 'Show Post',
        'list':menu,
        'post':db_data,
        'cat_selected':0
        }
    return render(request, 'main/post.html', data)

class Show_Post(DetailView):
    #model = Worker
    template_name = 'main/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'
    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        post = contex['object'].title
        contex['title'] = post
        return contex
    def get_object(self, queryset=None):
        return get_list_or_404(Worker.published, slug=self.kwargs[self.slug_url_kwarg])[0]



class Show_tag(ListView):
    model = TagModel
    template_name = 'main/index.html'
    def get_queryset(self):
        data = Worker.published.filter(tags__slug=self.kwargs['tag_slug'])
        return data
    
    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        tag = contex['view'].kwargs
        contex['title'] = f'tag: {tag['tag_slug']}'
        contex['post'] = contex['worker_list']
        contex['tags_bool'] = 1
        return contex



def page_not_found(request:HttpRequest, exception):
    return render(request, 'main/not_found.html')
    