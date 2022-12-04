from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone

from .models import User

def createForm(request):
    return render(request, 'users/createForm.html')

def create(request):
    user = User(username=request.POST['username'], password=request.POST['password'], created_date=timezone.now())
    user.save()
    return HttpResponse(F"200. created user {user.id} {user}")

def login(request, pk):
    return HttpResponse(f"200. You're at login {pk}.")

def logout(request, pk):
    return HttpResponse(f"200. You're at logout {pk}.")

def get(request, pk):
    user = get_object_or_404(User, pk=pk)
    return HttpResponse(f"200. Fetched {user}.")
