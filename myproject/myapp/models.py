from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Pakage(models.Model):
    location  =models.CharField(max_length=100)
    image=models.ImageField(upload_to='image/')
    price=models.IntegerField()
    Dates=models.DateField()
    shortdescription=models.TextField()
    
    fulldescription=models.TextField()
    approved=models.BooleanField('Approved',default=False)
    
        

class UserRegister(models.Model):
    
    Firstname=models.CharField(max_length=50)
    Lastname=models.CharField(max_length=50)
    Username=models.CharField(max_length=50)
    Email=models.EmailField()
    Password=models.CharField(max_length=50)
    ConfirmPassword=models.CharField(max_length=50,default=True)

class VendorRegister(models.Model):
    Vendorname=models.CharField(max_length=50)
    Email=models.EmailField()
    Password=models.CharField(max_length=50)
    ConfirmPassword=models.CharField(max_length=50,default=True)

class TravelBook(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)

    email=models.EmailField()
    phone=models.IntegerField()
    destination=models.CharField(max_length=50)
    

    
