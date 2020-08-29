from datetime import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from accounts.models import Profile


class SignUpForm(UserCreationForm):
    # first_name = forms.CharField(max_length=100, help_text='first Name')
    # last_name = forms.CharField(max_length=100, help_text='Last Name')
    email = forms.EmailField(max_length=150, help_text='Email')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


YEARS = [x for x in range(1940, 2021)]


class ProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=150)
    date_of_birth = forms.DateField() #widget=forms.SelectDateWidget(years=YEARS)

    class Meta:
        model = Profile
        fields = ('username', 'first_name', 'last_name', 'date_of_birth', 'email')
