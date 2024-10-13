from django.urls import path
from . import views

urlpatterns = [
    path('', views.city_list, name='city_list'),
    path('attractions/', views.attraction_list, name='attraction_list'),
    path('restaurants/', views.restaurant_list, name='restaurant_list'),
    path('hotels/', views.hotel_list, name='hotel_list'),
]
