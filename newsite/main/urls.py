from django.urls import path, register_converter
from . import views
from . import converters
#from django.contrib.staticfiles import views as vi
#UpdatePage
register_converter(converters.FourDigitYearConverter, 'year4')
urlpatterns = [
    path('', views.IndexHome.as_view(), name='home_name'),
    path('about/', views.about, name='about_name'),
    path('addpage/', views.AddPage.as_view(), name='add_name'),
    path('contacts/', views.contacts, name='contacts_name'),
    path('sign_in/', views.sign, name='sign_name'),
    path('category/<slug:cat_slug>/', views.Show_cat.as_view(), name='category'),
    path('post/<slug:post_slug>/', views.Show_Post.as_view(), name='show'),
    path('tag/<slug:tag_slug>/', views.Show_tag.as_view(), name='show_tag'),
    path('edit/<int:pk>/', views.UpdatePage.as_view(), name='update'),
    path('delete/<int:pk>/', views.DeletePost.as_view(), name='delete')
]
