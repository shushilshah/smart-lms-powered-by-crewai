from smart_lms.forms import *
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
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

    courses = Course.objects.filter(teacher=request.user)
    modules = Module.objects.filter(course__teacher=request.user)
    lessons = Lesson.objects.filter(module__course__teacher=request.user)
    context = {
        "courses": courses,
        "modules": modules,
        "lessons": lessons,
    }
    return render(request, "dashboards/teacher.html", context)

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



@login_required
def create_module_teacher(request, course_id):
    if request.user.userprofile.role != "teacher":
        raise PermissionDenied

    course = Course.objects.get(id=course_id, teacher=request.user)

    if request.method == "POST":
        form = ModuleForm(request.POST)
        if form.is_valid():
            module = form.save(commit=False)
            module.course = course
            module.save()
            return redirect("my_courses_teacher")
    else:
        form = ModuleForm()

    return render(request, "teacher/create_module_teacher.html", {
        "form": form,
        "course": course
    })


@login_required
def create_lesson_teacher(request, module_id):
    if request.user.userprofile.role != "teacher":
        raise PermissionDenied

    module = Module.objects.get(id=module_id)

    if request.method == "POST":
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.module = module
            lesson.save()
            return redirect("my_courses_teacher")

    else:
        form = LessonForm()

    return render(request, "teacher/create_lesson_teacher.html", {"form": form, "module": module})



@login_required
def course_detail_teacher(request, course_id):
    if request.user.userprofile.role != "teacher":
        raise PermissionDenied

    course = get_object_or_404(Course, id=course_id, teacher=request.user)
    modules = course.modules.all()

    context = {
        "course": course,
        "modules": modules
    }

    return render(request, "teacher/course_detail_teacher.html", context)


@login_required
def module_detail_teacher(request, module_id):
    if request.user.userprofile.role != "teacher":
        raise PermissionDenied
    
    module = get_object_or_404(Module, id=module_id, course__teacher=request.user)
    lessons = module.lessons.all()

    context = {
        "module": module,
        "lessons": lessons
    }

    return render(request, "teacher/module_detail_teacher.html", context)