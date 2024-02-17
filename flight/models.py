from django.utils import timezone

from django.db import models

# Create your models here.
# class bookings(models.Model):
#    name = models.CharField(max_length=200)
#    img = models.ImageField(upload_to='images')
#    From = models.CharField(max_length=200)
#    To = models.CharField(max_length=200)
#    Departing = models.DateTimeField(default=timezone.now)
#    Returning = models.DateTimeField(default=timezone.now)
#    Adults = models.SmallIntegerField()
#    Children = models.SmallIntegerField()
#    travelclass = models.CharField(max_length=100)
#    price = models.FloatField()

# class vehicle(models.Models):
class Flight(models.Model):
    airport1 = models.CharField(max_length=255)
    airport2 = models.CharField(max_length=255)
    departing_date = models.DateField()
    returning_date = models.DateField()

class booking(models.Model):
   email = models.CharField(max_length=200)
   first_name = models.CharField(max_length=200)
   last_name = models.CharField(max_length=200)
   airport1 = models.CharField(max_length=255)
   airport2 = models.CharField(max_length=255)
   departing_date = models.DateField()
   returning_date = models.DateField()
   adults = models.SmallIntegerField()
   Children = models.SmallIntegerField()
   price = models.FloatField()

# Create your models here.
class BookTickets(models.Model):
   name = models.CharField(max_length=200)
   email = models.CharField(max_length=200)
   phone = models.IntegerField()
   airport1 = models.CharField(max_length=255)
   airport2 = models.CharField(max_length=255)
   departing_date = models.CharField(max_length=200)
   returning_date = models.CharField(max_length=200)
   adults = models.IntegerField()
   children = models.IntegerField()
   price = models.DecimalField(max_digits=10, decimal_places=2)
