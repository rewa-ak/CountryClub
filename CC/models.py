from django.db import models

# Create your models here.

class Member(models.Model):
    First_name= models.CharField(max_length=15)
    Last_name= models.CharField(max_length=15)
    Date_of_birth= models.DateField()
    Email=models.EmailField()
    Membership_type= models.OneToOneField(Membership_type)
    Membership_deadline= models.DateField()
    Reservation= models.ManyToManyField(Reservation)

class Membership_type:
    Type=models.CharField(Max_length=30)
    Facilities=models.ManyToManyField(Facilities)
    Duration=models.DurationField()

class Facilities:
    facility=models.CharField(max_length=20)


class Reservation:
    Member=models.ManyToManyField(Member)
    Reserved_date=models.DateField()
    Reserved_time_start= models.TimeField()
    Reserved_time_end= models.TimeField()
    Facility=models.OneToOneField(Facilities)


