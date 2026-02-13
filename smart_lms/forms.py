from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from lms_app.models import Student, UserProfile, Course, Module, Lesson

class SignupForm(UserCreationForm):
    email = forms.EmailField()
    role = forms.ChoiceField(choices=UserProfile.ROLE_CHOICES)

    class Meta:
        model = User
        fields = ["username", "email", "role", "password1", "password2"]


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                "class": "form-control",
                "placeholder": " "
            })


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'is_published', 'student_slots', 'level', 'duration', 'learning_outcomes']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                "class": "form-control",
                "placeholder": " "
            })


class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ["title", "is_published"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                "class": "form-control"
            })


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ["title", "lesson_type", "content", "video", "external_link", "is_published"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})


class EditCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["title", "description", "is_published"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['roll_number', 'course', 'dob', 'phone', 'address']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'roll_number': forms.TextInput(attrs={'class': 'form-control'}),
            'course': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
