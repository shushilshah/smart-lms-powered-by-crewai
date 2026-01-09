from smart_lms.forms import SignupForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserProfile
# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()

            # create profile
            role = form.cleaned_data['role']
            UserProfile.objects.create(user=user, role=role)

            messages.success(request, "Your account has been created successfully! You can now login.")
            return redirect("login")
        
    else:
        form = SignupForm()

    context = {
        "form": form
    }
    return render(request, "accounts/signup.html", context)
