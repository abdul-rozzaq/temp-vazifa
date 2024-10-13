from django.db import models


from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    country = models.CharField(max_length=100)
    population = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Attraction(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='attractions')
    name = models.CharField(max_length=150)
    description = models.TextField()
    ticket_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='restaurants')
    name = models.CharField(max_length=150)
    cuisine_type = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return self.name


class Hotel(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='hotels')
    name = models.CharField(max_length=150)
    stars = models.PositiveIntegerField()
    price_per_night = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
