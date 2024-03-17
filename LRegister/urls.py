from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterUser, name='register'),
    path('login/', views.LoginUser, name='login'),
    path('', views.temp, name='temp'),
    path('logout/', views.logoutUser, name='logout')
]