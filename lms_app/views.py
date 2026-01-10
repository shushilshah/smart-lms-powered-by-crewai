from smart_lms.forms import SignupForm, CourseForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Course, UserProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

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


@login_required
def teacher_dashboard(request):
    if request.user.userprofile.role != 'teacher':
        raise PermissionDenied
    return render(request, "dashboards/teacher.html")

@login_required
def student_dashboard(request):
    if request.user.userprofile.role != "student":
        raise PermissionDenied

    return render(request, "dashboards/student.html")


@login_required
def create_course_teacher(request):
    if request.user.userprofile.role != "teacher":
         raise PermissionDenied
    
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.teacher = request.user
            course.save()
            return redirect("my_courses_teacher")
        
    else:
        form = CourseForm()

    return render(request, "teacher/create_course_teacher.html", {"form": form})


@login_required
def my_courses_teacher(request):
    if request.user.userprofile.role != "teacher":
        raise PermissionDenied

    courses = Course.objects.filter(teacher=request.user)
    return render(request, "teacher/my_courses_teacher.html", {"courses": courses})