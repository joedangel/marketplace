from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("200. You're at the listings index.")

def create(request):
    return HttpResponse("200. You're at create.")

def delete(request):
    return HttpResponse("200. You're at delete.")

def update(request):
    return HttpResponse("200. You're at update.")

def list(request):
    return HttpResponse("200. You're at list.")

def get(request):
    return HttpResponse("200. You're at get.")

# purchase? return? cancel? order_status? in new orders app?
