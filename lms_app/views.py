from smart_lms.forms import SignupForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth import authenticate, login, logout
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


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        remember_me = request.POST.get("remember_me")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # session base expiry logic
            if not remember_me:
                request.session.set_expiry(0)
            else:
                request.session.set_expiry(1209600) # 2 weeks

            # role based redirect
            role = user.userprofile.role
            if role == 'admin':
                return redirect('admin_dashboard')
            elif role == 'teacher':
                return redirect('teacher_dashboard')
            else:
                return redirect("student_dashboard")
            
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")