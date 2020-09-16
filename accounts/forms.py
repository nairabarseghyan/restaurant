from datetime import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from accounts.models import Profile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=150, help_text='Email')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


YEARS = [x for x in range(1940, datetime.now().year + 1)]


class ProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))

    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo']
