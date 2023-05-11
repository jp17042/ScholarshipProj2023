from django.shortcuts import render
from django.http import HttpResponse
from .models import InfoPersonal
# Create your views here.
def login(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(name, email, password)

        new_info = InfoPersonal()
        new_info.name = name
        new_info.email = email
        new_info.password = password


        new_info.save()


    return render(request, 'login/login.html')


