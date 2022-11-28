from django.urls import path

from . import views

app_name = 'listings'

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='index'),
    path('publish', views.publish, name='publish'),
    path('delete/<int:pk>', views.delete, name='index'),
    path('update/<int:pk>', views.update, name='index'),
    path('list', views.listings, name='index'),
    path('get/<int:pk>', views.get, name='index')
]