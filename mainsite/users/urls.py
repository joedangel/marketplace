from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('createForm', views.createForm, name='createForm'),
    path('create', views.create, name='create'),
    path('loginForm', views.loginForm, name='loginForm'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('<int:pk>/get', views.get, name='get')
]