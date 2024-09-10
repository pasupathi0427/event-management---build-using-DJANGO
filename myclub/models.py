from django.db import models
from django.contrib.auth.models import User


class Venue(models.Model):
    name = models.CharField('Venue Name' , max_length=120)
    address =models.TextField('Venue Address',max_length=200)
    phone = models.CharField('Contact Number', max_length=120)
    pincode= models.CharField('Pincode' , max_length=7 , default='63200')
    web = models.URLField('Web address')
    email = models.EmailField('Email Address')
    image = models.ImageField( null=True, blank=True , default = "" ,upload_to='images/')

    def __str__(self) -> str:
        return self.name

class Clubusers(models.Model):
    first_name  = models.CharField('First Name', max_length=120)
    last_name = models.CharField('Last Name', max_length=120)
    email = models.EmailField('Email Address')

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name
    
class Events(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event date')
    Venue = models.ForeignKey(Venue , blank=True , null= True , on_delete=models.CASCADE)
    manager =  models.ForeignKey(User , blank=True , null=True , on_delete= models.SET_NULL)
    description = models.TextField('Description')
    attendees = models.ManyToManyField(Clubusers , blank= True)

    def __str__(self) -> str:
        return self.name
    