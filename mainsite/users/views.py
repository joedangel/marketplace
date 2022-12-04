from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone

from .models import User

def createForm(request):
    return render(request, 'users/createForm.html')

def create(request):
    try:
        get_object_or_404(User, username=request.POST['username'])
    except:
        return HttpResponse('400. Username unavailable.')

    user = User(username=request.POST['username'], password=request.POST['password'], created_date=timezone.now())
    user.save()

    response = HttpResponse(F"200. created user {user.id} {user}")
    response.set_cookie('user_id', user.id)
    return response

def loginForm(request):
    return render(request, 'users/loginForm.html')

def login(request):
    user = get_object_or_404(User, username=request.POST['username'])
    if user.password != request.POST['password']:
        return HttpResponse(f"400. Wrong password.")

    response = HttpResponse(f"200. You've logged in {user}.")
    response.set_cookie('user_id', user.id)
    return response

def logout(request):
    try:
        active_user_id = request.COOKIES['user_id']
        response = HttpResponse(f"200. You've logged out {active_user_id}.")
        response.delete_cookie('user_id')
        return response
    except KeyError:
        return HttpResponse(f"500. Failed to logout.")

def get(request, pk):
    user = get_object_or_404(User, pk=pk)
    return HttpResponse(f"200. Fetched {user}.")
