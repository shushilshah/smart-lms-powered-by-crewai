from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from lms_app.models import UserProfile

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











        # def save(self, commit=True):
        # user = super().save(commit=False)
        # user.email = self.cleaned_data["email"]
        # if commit:
        #     user.save()
        # return user
