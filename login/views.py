from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

def login_view(request):
    #IF the request method is a POST method
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  # Replace 'home' with the name of your home page URL pattern
        else:
            # Authentication failed, display an error message

            return render(request, 'login/login.html')
    else:
        return render(request, 'login/login.html')



