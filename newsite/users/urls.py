from django.urls import path
from . import views
#from django.contrib.staticfiles import views as vi
#UpdatePage
urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
