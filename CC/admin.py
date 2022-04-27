from django.contrib import admin
from .models import Member, Membership_type, Facilities, Reservation

# Register your models here.

admin.site.register(Facilities)
admin.site.register(Membership_type)
admin.site.register(Member)
admin.site.register(Reservation)