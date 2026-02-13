from . import views
from django.urls import path


urlpatterns = [
    path("generate-course/", views.generate_course, name="generate_course"),
    path("generator/", views.course_generator_page, name="course_generator_page")
]
