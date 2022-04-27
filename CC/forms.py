import datetime
from django import forms
import django.forms
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from CC.models import Member, Reservation
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = ['First_name','Last_name', 'Date_of_birth', 'Email', 'Membership_type']
        labels = {'First_name': _('First Name'), 'Last_name': _('Last Name'), 'Date_of_birth':_('Date of birth'), 'Email':_('Email'), 'Membership_type':_('Membership types')}


class ReservationForm(ModelForm):
    class Meta:
        model= Reservation
        fields = ['Reserved_date', 'Reserved_time_start', 'Court_number' ]
        labels = {'Reserved_date': _('Date'), 'Reserved_time_start':_('Time'), 'Court_number':_('Court')}

class UserForm(UserCreationForm):
        email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.', required=True)
        class Meta:
            model= User
            fields = ['username', 'email', 'password1', 'password2']
            labels = { 'username': _('Username'), 'email':_('Email'), 'password1':_('Password'), 'password2':_('Repeat password')}

        def save(self, commit=True):
            user = super(UserCreationForm, self).save(commit=False)
            user.email = self.cleaned_data["email"]
            if commit:
                user.save()
            return user
