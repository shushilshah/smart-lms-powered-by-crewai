from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'role','created_at']
    list_filter = ['role']
    search_fields = ['user']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'teacher', 'is_published', 'created_at']
    list_filter = ['is_published', 'teacher']
    search_fields = ['title', 'description']

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['title','is_published', 'created_at']
    list_filter = ['is_published', 'course']
    search_fields = ['title']


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    lsit_display = ['title', 'module', 'lesson_type', 'is_published', 'created_at']
    list_filter = ['is_published', 'lesson_type', 'module']
    search_fields = ['title', 'module']