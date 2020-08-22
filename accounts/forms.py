from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from quorum.exceptions import ValidationError

from .models import Profile


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')


