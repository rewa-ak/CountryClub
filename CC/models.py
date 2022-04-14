from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class Facilities(models.Model):
    facility=models.CharField(max_length=20)

class Membership_type(models.Model):
    Type=models.CharField(max_length=30)
    Facilities=models.ForeignKey(Facilities,on_delete=models.SET_NULL)
    Duration=models.DurationField()

class Member(models.Model):
    First_name= models.CharField(max_length=15)
    Last_name= models.CharField(max_length=15)
    Date_of_birth= models.DateField()
    Email=models.EmailField(unique=True)
    Membership_type= models.OneToOneField(Membership_type,on_delete=models.CASCADE)
    Membership_deadline= models.DateField()
    

class Reservation(models.Model):
    Member=models.ManyToManyField(Member)
    Reserved_date=models.DateField()
    Reserved_time_start= models.TimeField()
    Reserved_time_end= models.TimeField()
    Facility=models.OneToOneField(Facilities,on_delete=models.CASCADE)
    Court_number= models.IntegerField()


