from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.dispatch import receiver
from django.db.models.signals import post_save


class UserProfile(models.Model):
    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("teacher", "Teacher"),
        ("student", "Student")
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="userprofile")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=50)
    course = models.CharField(max_length=255)
    dob = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255)


    def __str__(self):
        return self.user.get_full_name()

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, blank=True)



@receiver(post_save, sender=User)
def create_student(sender, instance, created, **kwargs):
    if created:
        try:
            profile = instance.userprofile  # access UserProfile via related_name
            if profile.role == "student":
                Student.objects.create(user=instance)
        except UserProfile.DoesNotExist:
            pass 
    

# @receiver(post_save, sender=User)
# def save_student(sender, instance, **kwargs):
#     instance.student.save()



class Course(models.Model):
    LEVEL = (
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced")
    )
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255, blank=True)
    student_slots = models.PositiveIntegerField(default=10)
    level = models.CharField(choices=LEVEL, max_length=20)
    duration = models.CharField(max_length=100)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={"userprofile__role": "teacher"}, related_name="courses")
    learning_outcomes = models.TextField(default="can perform better analysis")
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



class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ("user", "course")


class LessonProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ("user", "lesson")
