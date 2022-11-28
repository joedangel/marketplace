from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Listing

def index(request):
    return HttpResponse("200. You're at the listings index.")

def create(request):
    return render(request, 'listings/create.html')

def publish(request):
    return HttpResponse('Publish 200')

def delete(request):
    return HttpResponse("200. You're at delete.")

def update(request):
    return HttpResponse("200. You're at update.")

def listings(request):
    listings = Listing.objects.order_by('id')
    context = {'listings': listings}
    return render(request, 'listings/listings.html', context)

def get(request, pk):
    print(pk)
    listing = get_object_or_404(Listing, pk=pk)
    return render(request, 'listings/listing.html', {'listing': listing})

# purchase? return? cancel? order_status? in new orders app?
