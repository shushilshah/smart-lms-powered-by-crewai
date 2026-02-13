from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile, Student

# Trigger Student creation AFTER UserProfile is created


@receiver(post_save, sender=UserProfile)
def create_student_after_profile(sender, instance, created, **kwargs):
    if created and instance.role == "student":
        # Only create Student if not already exists
        Student.objects.get_or_create(user=instance.user)
