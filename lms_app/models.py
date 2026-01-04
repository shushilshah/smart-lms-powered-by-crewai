from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255, blank=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Module(models.Model):
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Lesson(models.Model):
    LESSON_TYPES = (
        ('video', 'Video'),
        ('pdf', 'PDF/Document'),
        ('text', 'Text'),
        ('external', 'External Link')
    )
    module = models.ForeignKey(Module, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    lesson_type = models.CharField(max_length=30, choices=LESSON_TYPES)
    content = models.TextField(blank=True)
    external_link = models.FileField(upload_to='lessons/', blank=True)
    video = models.URLField(blank=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



