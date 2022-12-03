from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Listing
from django.utils import timezone

def index(request):
    return render(request, 'listings/generic.html', {'msg': "200. You're at the listings index."})

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

    return render(request, 'listings/generic.html', {'msg': f"{listing} created successfully"})

def delete(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    listing.delete()
    return render(request, 'listings/generic.html', {'msg': f"200. Deleted {pk}."})

def update(request, pk):
    return HttpResponse(f"200. You're at update {pk}.")

def listings(request):
    listings = Listing.objects.order_by('id')
    context = {'listings': listings}
    return render(request, 'listings/listings.html', context)

def get(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    return render(request, 'listings/listing.html', {'listing': listing})

# purchase? return? cancel? order_status? in new orders app?
