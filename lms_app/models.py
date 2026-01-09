from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError




class UserProfile(models.Model):
    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("teacher", "Teacher"),
        ("student", "Student")
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="userprofile")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)



class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255, blank=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={"userprofile__role": "teacher"}, related_name="courses")
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
    external_link = models.URLField(blank=True)
    video = models.URLField(blank=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.lesson_type == 'video' and not self.video:
            raise ValidationError("Video URL is required for video lessons.")
        
        if self.lesson_type == 'external' and not self.external_link:
            raise ValidationError("External link is required")
        
        if self.lesson_type == 'text' and not self.content:
            raise ValidationError("Content is required for text lessons.")
        

    def __str__(self):
        return self.title



