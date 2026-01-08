from django.shortcuts import render
from smart_lms.forms import SignupForm
from django.contrib import messages
from django.shortcuts import render, redirect
# Create your views here.

def singup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created successfully! You can now login.")
            return redirect("login")
        
        else:
            form = SignupForm()

        context = {
            "form": form
        }
        return render(request, "accounts/signup.html", context)
