from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Listing
from django.utils import timezone

def index(request):
    return HttpResponse("200. You're at the listings index.")

def create(request):
    return render(request, 'listings/create.html')

def publish(request):
    data = request.POST
    listing = Listing(
        item_type=data['type'],
        item_color=data['color'],
        item_brand=data['brand'],
        item_condition=data['condition'],
        item_material=data['material'],
        item_price=float(data['price']),
        listing_date=timezone.now())
    listing.save()

    return HttpResponse(f"{listing} created successfully")

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
