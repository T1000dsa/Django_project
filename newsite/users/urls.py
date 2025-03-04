from django.urls import path
from . import views
#from django.contrib.staticfiles import views as vi
#UpdatePage
urlpatterns = [
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', views.LogoutUser.as_view(), name='logout'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('profile/', views.ProfileUser.as_view(), name='profile'),
]
