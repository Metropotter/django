from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import secrets
from .models import UserProfile

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Auto-verify since we don't have email
            UserProfile.objects.create(
                user=user, 
                email_verified=True,  # ✅ Auto-verified
                verification_token=''
            )
            
            messages.success(request, 'Registration successful! You can now login.')
            return redirect('languages_app:user_login')
    else:
        form = UserCreationForm()
    return render(request, 'languages_app/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Skip email verification check - direct login
            login(request, user)
            
            # Redirect superusers to admin, regular users to forum
            if user.is_superuser:
                return redirect('/admin/')  # Superusers go to admin
            else:
                return redirect('languages_app:forum_home')  # Regular users go to forum
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'languages_app/login.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('languages_app:home')

def verify_email(request, token):
    try:
        profile = UserProfile.objects.get(verification_token=token)
        profile.email_verified = True
        profile.verification_token = ''
        profile.save()
        messages.success(request, 'Email verified successfully! You can now login.')
    except UserProfile.DoesNotExist:
        messages.error(request, 'Invalid verification token.')
    
    return redirect('login')