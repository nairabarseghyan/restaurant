# accounts views
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.utils.encoding import force_text
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views import View
from django.views.generic import UpdateView

from . import forms, models
from .models import Profile
from .tokens import account_activation_token
from django.template.loader import render_to_string
from .forms import SignUpForm, ProfileForm
from .tokens import account_activation_token


def home_view(request):
    return render(request, 'home.html')


def activation_sent_view(request):
    return render(request, 'activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.signup_confirmation = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'activation_invalid.html')


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Please Activate Your Account'
            message = render_to_string('activation_request.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def profile(request):
    user = request.user
    if user.is_authenticated:
        p_user = Profile.objects.get(user=user)
    else:
        return "Sing in"
    return render(request, 'profile.html', {'profile': p_user})


def edit_profile(request):
    user = request.user
    form = ProfileForm(request.POST or None,
                       initial={'username': user.username, 'email': user.profile.email, 'first_name': user.profile.first_name,
                                'last_name': user.profile.last_name, 'date_of_birth': user.profile.date_of_birth})
    if request.method == 'POST':
        if form.is_valid():
            user.username = request.POST['username']
            user.first_name = request.POST['first_name']
            user.profile.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.profile.last_name = request.POST['last_name']
            user.date_of_birth = request.POST['date_of_birth']
            user.profile.date_of_birth = request.POST['date_of_birth']
            user.profile.email = request.POST['email']
            user.email = request.POST['email']

            user.save()
            return HttpResponseRedirect('%s' % (reverse('profile')))

    context = {
        "form": form
    }

    return render(request, "edit_profile.html", context)
