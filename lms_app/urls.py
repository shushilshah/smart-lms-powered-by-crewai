from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup_view, name='signup'),
    path("login/", views.login_view, name='login'),
    path("logout/", views.logout_view, name='logout'),
    path("teacher/dashboard/", views.teacher_dashboard, name="teacher_dashboard"),
    path("student/dashboard/", views.student_dashboard, name="student_dashboard"),
    path("teacher/create-course/", views.create_course_teacher, name="create_course_teacher"),
    path("teacher/my-courses/", views.my_courses_teacher, name="my_courses_teacher"),
]
