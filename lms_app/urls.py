from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("signup/", views.signup_view, name='signup'),
    path("login/", views.login_view, name='login'),
    path("logout/", views.logout_view, name='logout'),
    path("teacher/dashboard/", views.teacher_dashboard, name="teacher_dashboard"),
    path("student/dashboard/", views.student_dashboard, name="student_dashboard"),
    path("teacher/create-course/", views.create_course_teacher, name="create_course_teacher"),
    path("teacher/my-courses/", views.my_courses_teacher, name="my_courses_teacher"),
    path("teacher/course/<int:course_id>/module-create/", views.create_module_teacher, name="create_module_teacher"),
    path("teacher/module/<int:module_id>/lesson-create/", views.create_lesson_teacher,name="create_lesson_teacher"),
    path("teacher/course/<int:course_id>/", views.course_detail_teacher, name="course_detail_teacher"),
    path("teacher/module/<int:module_id>/", views.module_detail_teacher, name="module_detail_teacher"),
    path("teacher/course/<int:course_id>/edit-course/", views.edit_course_teacher, name="edit_course_teacher"),
    path("all-courses/", views.all_courses_student, name="all_courses"),
    path("student/course/<int:course_id>/", views.course_detail_student, name="course_detail_student"),
    path("student/course/<int:course_id>/enroll/", views.enroll_course_student, name="enroll_course_student"),
    path("student/my-courses/", views.my_courses_student, name="my_courses_student"),
    path("student/course/<int:course_id>/lesson_detail_student/", views.lesson_detail_student, name="lesson_detail_student"),
    path("student/profile/", views.student_profile, name="student_profile"),
    path("teacher/profile/", views.teacher_profile, name="teacher_profile"),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
