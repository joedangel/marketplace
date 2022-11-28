from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='index'),
    path('delete/{pk}', views.delete, name='index'),
    path('update/{pk}', views.update, name='index'),
    path('list', views.list, name='index'),
    path('get/{pk}', views.get, name='index')
]