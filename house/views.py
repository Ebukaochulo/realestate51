from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    latest = Housee.objects.order_by('-date_added')[0:3]
    billboard = Housee.objects.order_by('-date_added')[0:4]
    context = {'latest':latest, 'billboard':billboard}
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def property_grid(request):
    houses = Housee.objects.all
    context = {'houses':houses}
    return render(request, 'property-grid.html', context)

def property_single(request, pk):
    house = Housee.objects.get(id=pk)
    amenities = Amenities.objects.all
    
    context ={'house':house, 'amenities':amenities}
    return render(request, 'property-single.html', context)

def search(request):
    if request.method == 'POST':
        city     =   request.POST['city']
        location =   Housee.objects.filter(location__contains=city)
        context  =   {'location':location}
        return render(request, "search.html", context)
    else :
        return render(request, "search.html", context)
