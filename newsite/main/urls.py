from django.urls import path, register_converter
from . import views
from . import converters
#from django.contrib.staticfiles import views as vi

register_converter(converters.FourDigitYearConverter, 'year4')
urlpatterns = [
    path('', views.index_http, name='home_name'),
    path('about/', views.about, name='about_name'),
    path('add page/', views.add, name='add_name'),
    path('contacts/', views.contacts, name='contacts_name'),
    path('sign_in/', views.sign, name='sign_name'),
    path('category/<slug:cat_slug>/', views.show_cat, name='category'),
    path('post/<slug:post_slug>/', views.show_post, name='show'),
    path('tag/<slug:tag_slug>/', views.show_tag_postlist, name='show_tag')
]
