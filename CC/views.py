from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request handler
def home(request):
    return render(request,'Home.html')
    
def user_registration(request):
    return render(request, 'Membership_registration.html')


