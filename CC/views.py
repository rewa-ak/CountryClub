import email
import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import MemberForm, Reservation, ReservationForm, UserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.template import loader
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# request handler
def home(request):
    return render(request,'Home.html')

@login_required  
def user_registration(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            memberForm = form.cleaned_data 
            First_name = memberForm['First_name']
            Last_name = memberForm['Last_name']
            Date_of_birth = memberForm['Date_of_birth']
            Email= memberForm['Email']
            Membership_type = memberForm['Membership_type']
            Membership_deadline = Date_of_birth
            Member.objects.create(First_name=First_name,Last_name=Last_name,Date_of_birth=Date_of_birth,Email=Email,Membership_type=Membership_type,Membership_deadline=Membership_deadline)
            return render(request, 'Home.html')
    else:
        form = MemberForm()
    return render(request, 'Membership_registration.html',{'form':form})
    

@login_required
def club_calender(request): #add dates to a calender
    reservations= Reservation.objects.get()
    return render(request, 'Club_calender.html')   

def complaint(request):
    return render(request, 'Complaint.html')

@login_required
def facility_reservation(request):

    return render(request, 'Facility_reservation.html')

@login_required
def tennis_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            tennisform = form.cleaned_data
            email = request.user.email
            member= Member.get(email=email)
            Reserved_date = tennisform['Reserved_date']
            Reserved_time_start= tennisform['Reserved_time_start']
            Reserved_time_end= Reserved_time_start+60
            Facility= Facility.facility[1]
            Court_number=tennisform['Court_number']
            Reservation.objects.create(Member=member,Reserved_date=Reserved_date,Reserved_time_start=Reserved_time_start,Reserved_time_end=Reserved_time_end,Facility=Facility, Court_number=Court_number)
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
            email = request.user.email
            member= Member.get(email=email)
            Reserved_date = golfform['Reserved_date']
            Reserved_time_start= golfform['Reserved_time_start']
            Reserved_time_end= Reserved_time_start+60
            Facility= Facility.facility[0]
            Court_number=golfform['Court_number']
            Reservation.objects.create(Member=member,Reserved_date=Reserved_date,Reserved_time_start=Reserved_time_start,Reserved_time_end=Reserved_time_end,Facility=Facility, Court_number=Court_number)
            return render(request, 'Home.html')
    else:
        form = ReservationForm()
    return render(request, 'Golf_reservation.html',{'form':form})

@login_required
def member_information(request):
    em=request.user.email
    try:
        member_info= Member.objects.get(email=em)
        return render(request, 'Member_information.html', {
            'member_found': True,
            'fname': member_info.First_name,
            'lname': member_info.Last_name,
            'Date_of_birth': member_info.Date_of_birth,
            'membership': member_info.Membership_type,
            'deadline': member_info.Membership_deadline
        })
    except Exception as exc:
        return render(request, 'Member_information.html',{
            'member_found': False
        })

def news(request):
    return render(request, 'News.html')

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email= form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password, email=email)
            login(request, user)
            return redirect('home')
    else:
        form = UserForm()
        signup=False
    return render(request, 'Signup.html', {'form': form, 'signup':False})

