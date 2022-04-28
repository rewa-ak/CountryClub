from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('home/', views.home),
    path('register/',views.user_registration),
    path('memberinfo/',views.member_information),
    path('clubcalendar/',views.club_calender),
    path('submit a complaint/', views.complaint),
    path('Facility reservation/', views.facility_reservation),
    path('news/', views.news),
    path('tennis_reservation/', views.tennis_reservation),
    path('golf_reservation/', views.golf_reservation),
    path('Sign up/',views.signup),
    path('MemberUpdate/', views.MemberUpdate),
    path('MemberDelete/', views.MemberDelete),
    path('ReservationUpdate/<int:id>', views.ReservationUpdate, name='ReservationUpdate'),
    path('ReservationDelete/<int:id>', views.ReservationDelete, name='ReservationDelete')
]

