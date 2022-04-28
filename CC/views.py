from asyncio.windows_events import NULL
import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from .models import *
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.template import loader
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
# request handler
def home(request):
    return render(request,'Home.html')

@login_required  
def user_registration(request):                                         #done
    if Member.objects.filter(user=request.user).exists():
        return render(request, 'Membership_registration.html', {'register': True, 'message':'You are already a member!'})
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            memberForm = form.cleaned_data 
            First_name = memberForm['First_name']
            Last_name = memberForm['Last_name']
            Date_of_birth = memberForm['Date_of_birth']
            Membership_type = memberForm['Membership_type']
            Membership_deadline = datetime.date.today() + datetime.timedelta(weeks=52)
            Member.objects.create(user=request.user,First_name=First_name,Last_name=Last_name,Date_of_birth=Date_of_birth,Membership_type=Membership_type,Membership_deadline=Membership_deadline)
        
            return render(request, 'Membership_registration.html', {'register': True, 'message':'Registration successful!'})
    else:
        form = MemberForm()
    return render(request, 'Membership_registration.html', {'form':form})
    

@login_required
def club_calender(request): #add dates to a calender
    reservations= Reservation.objects.all()
    return render(request, 'Club_calender.html', {'reservations': reservations})   

def complaint(request):
    return render(request, 'Complaint.html')

@login_required
def facility_reservation(request):
    details= []
    if Reservation.objects.filter(Member=Member.objects.get(user=request.user)).exists():
        details=Reservation.objects.filter(Member=Member.objects.get(user=request.user))
    return render(request, 'Facility_reservation.html', {'details': details})

@login_required
def tennis_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            tennisform = form.cleaned_data
            member= Member.objects.filter(user=request.user)
            Reserved_date = tennisform['Reserved_date']
            Reserved_time_start= tennisform['Reserved_time_start']
            Reserved_time_end= datetime.time(Reserved_time_start.hour+1)
            Facility= Facilities.objects.get(facility='Tennis')
            Court_number=tennisform['Court_number']
            instance=Reservation.objects.create(Reserved_date=Reserved_date,Reserved_time_start=Reserved_time_start,Reserved_time_end=Reserved_time_end,Facility=Facility, Court_number=Court_number)
            instance.Member.set(member)
            return render(request, 'Home.html')
            form.save()
    else:
        form = ReservationForm()
    return render(request, 'Tennis_reservation.html',{'form':form})

@login_required
def golf_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            golfform = form.cleaned_data
            member= Member.objects.filter(user=request.user)
            Reserved_date = golfform['Reserved_date']
            Reserved_time_start= golfform['Reserved_time_start']
            Reserved_time_end= datetime.time(Reserved_time_start.hour+1)
            Facility= Facilities.objects.get(facility='Golf')
            Court_number=golfform['Court_number']
            instance=Reservation.objects.create(Reserved_date=Reserved_date,Reserved_time_start=Reserved_time_start,Reserved_time_end=Reserved_time_end,Facility=Facility, Court_number=Court_number)
            instance.Member.set(member)
            return render(request, 'Home.html')
    else:
        form = ReservationForm()
    return render(request, 'Golf_reservation.html',{'form':form})

@login_required
def member_information(request):                               #done
    if Member.objects.filter(user=request.user).exists():
        member_info= Member.objects.get(user=request.user)
        return render(request, 'Member_information.html', {
            'member_found': True,
            'fname': member_info.First_name,
            'lname': member_info.Last_name,
            'Date_of_birth': member_info.Date_of_birth,
            'membership': member_info.Membership_type,
            'deadline': member_info.Membership_deadline
        })
    else:
        return render(request, 'Member_information.html',{
            'member_found': False
        })



def news(request):
    return render(request, 'News.html')

def signup(request):                                #done
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email= form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password, email=email)
            login(request, user)
            return render(request,'Signup.html', {'signup':True})
    else:
        form = UserForm()
        #signup=False
    return render(request, 'Signup.html', {'form': form, 'signup':False})

@login_required
def MemberUpdate(request):
    if request.method == 'POST':
        context={'success':False}
        member=Member.objects.get(user=request.user)
        form=MemberUpdateForm(request.POST,instance=member)
        if form.is_valid:
            form.save()
            member=Member.objects.all()
            context={'success':True}
            return render(request,'MemberUpdate.html',context)
    else:
        form=MemberUpdateForm()
    return render(request,'MemberUpdate.html', {'form': form})

@login_required
def MemberDelete(request):
    if request.method=="POST":
        Member.objects.filter(user=request.user).delete()
        return render(request,'MemberDelete.html',{'success':True}) 
    return render(request,'MemberDelete.html')  

@login_required
def ReservationUpdate(request, id):
    if request.method=="POST":
        reservation=Reservation.objects.get(id=id)
        form=ReservationUpdateForm(request.POST,instance=reservation)
        if form.is_valid:
            form.save()
            reservation=Reservation.objects.all()
            return render(request,'ReservationUpdate.html',{'success':True})
    else:
        form=ReservationUpdateForm()
    return render(request,'ReservationUpdate.html', {'form': form})

@login_required
def ReservationDelete(request, id):
    if request.method=="POST":
        Reservation.objects.filter(id=id).delete()
        return render(request,'ReservationDelete.html',{'success':True})
    return render(request,'ReservationDelete.html') 

def Complaints(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'Complaint.html',{'success':True})
    else:
        form=ComplaintForm()
    return render(request,'Complaint.html',{'form':form})