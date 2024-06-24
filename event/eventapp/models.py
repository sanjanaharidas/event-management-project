from django.db import models

# Create your models here.
class Event(models.Model):
    img=models.ImageField(upload_to="images",null=True,blank=True)
    name=models.CharField(max_length=50)
    desc=models.CharField(max_length=500)
    def __str__(self):
        return self.name


class Booking(models.Model):
    Customer_name=models.CharField(max_length=100)
    Customer_phone=models.CharField(max_length=12)
    Event_name=models.ForeignKey(Event,on_delete=models.CASCADE)
    Booking_date=models.DateField()
    Booked_on=models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.Customer_name} - {self.Event_name.name}'
