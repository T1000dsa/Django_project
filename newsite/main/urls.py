from django.urls import path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, 'year4')
#menu = ['about site', 'add page', 'contacts', 'sign in']
urlpatterns = [
    path('', views.index_http, name='home_name'),
    path('about/', views.about, name='about_name'),
    path('add page/', views.add, name='add_name'),
    path('contacts/', views.contacts, name='contacts_name'),
    path('sign_in/', views.sign, name='sign_name'),
]
