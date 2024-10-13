from django.shortcuts import render
from .models import City, Attraction, Restaurant, Hotel

def city_list(request):
    cities = City.objects.all()
    return render(request, 'city_list.html', {'cities': cities})

def attraction_list(request):
    attractions = Attraction.objects.all()
    return render(request, 'attraction_list.html', {'attractions': attractions})

def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurant_list.html', {'restaurants': restaurants})

def hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotel_list.html', {'hotels': hotels})
