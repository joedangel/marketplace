from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('createForm', views.createForm, name='createForm'),
    path('create', views.create, name='create'),
    path('<int:pk>/login', views.login, name='login'),
    path('<int:pk>/logout', views.logout, name='logout'),
    path('<int:pk>/get', views.get, name='get')
]