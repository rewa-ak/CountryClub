from tkinter.tix import MAX
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class Facilities(models.Model):

    facility=models.CharField(max_length=20, unique=False)

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.facility

class Membership_type(models.Model):
    Type=models.CharField(max_length=30)
    Facilities=models.ForeignKey(Facilities,on_delete=models.CASCADE)
    Duration=models.DurationField()

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return  '{0} {1}'.format(self.Facilities, self.Type )

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, unique=True)
    First_name= models.CharField(max_length=15)
    Last_name= models.CharField(max_length=15)
    Date_of_birth= models.DateField()
    Membership_type= models.ForeignKey(Membership_type, on_delete=models.SET_NULL, null=True)
    Membership_deadline= models.DateField()

    @property
    def is_overdue(self):
        if self.Membership_deadline and date.today() > self.Membership_deadline:
            return True
        return False
     
    def __str__(self):
        """String for representing the Model object."""
        return '{0} {1}'.format(self.First_name, self.Last_name)

class Reservation(models.Model):
    Member=models.ManyToManyField(Member)
    Reserved_date=models.DateField()
    Reserved_time_start= models.TimeField()
    Reserved_time_end= models.TimeField()
    Facility=models.ForeignKey(Facilities,on_delete=models.CASCADE)
    Court_number= models.IntegerField(default=1)

    def __str__(self):
        """String for representing the Model object."""
        return str(self.Facility)+' Court '+str(self.Court_number)+' '+str(self.Reserved_date)+' from '+str(self.Reserved_time_start)+' to '+str(self.Reserved_time_end)

class Complaints(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.EmailField()
    Telephone=models.IntegerField()
    Complaint=models.CharField(max_length=1000)
