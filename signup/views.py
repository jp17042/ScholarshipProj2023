# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import SignupForm
from django.db.models.signals import post_save
from django.core.management import call_command
from .untils import create_user_database
from django.contrib.auth import get_user_model
from .signals import create_user_table
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user = User.objects.create_user(username=username, password=password, email=email)
            # Get the user's ID after signup
            user_id = user.pk

            # Call the function to create the user-specific table
            create_user_table(user_id)
            return redirect('/')
    else:
        form = SignupForm()
    return render(request, 'signup/signup.html', {'form': form})

 

