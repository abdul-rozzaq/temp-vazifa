from django import template

register = template.Library()

from project.models import City, Attraction, Restaurant, Hotel


@register.simple_tag
def city_count():
    return City.objects.count()


@register.simple_tag
def attraction_count():
    return Attraction.objects.count()


@register.simple_tag
def restaurant_count():
    return Restaurant.objects.count()


@register.simple_tag
def hotel_count():
    return Hotel.objects.count()
