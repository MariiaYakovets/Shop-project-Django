from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from requests import Request
import json
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
# Create your views here.

def show_user(request):
    if request.user.is_authenticated:
        username = request.user.username
        context = {'username': username}   
        return render(request=request, template_name= 'user.html', context=context)
    else:
        return redirect('login')

def login_user(request):
    if request.method == 'POST':
        byte_data = request.body
        data = json.loads(byte_data.decode("utf-8"))
        username = data["username"]
        password = data["password"]
        auth_user = authenticate(request=request, username= username, password= password)
        if auth_user is not None:
           login(request=request, user= auth_user)
           return redirect('user')
        else:
            return HttpResponse(status=401, reason="Wrong username or password")
    elif request.method == 'GET':
        return render(request=request, template_name= 'login.html')
    
def loguot_user(request):
    logout(request=request)
    return redirect('login')

def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            byte_data = request.body
            data = json.loads(byte_data.decode("utf-8"))
            password = data['password']
            user = User.objects.get(username= request.user.username)
            user.set_password(password)
            user.save()
            login(request=request, user= user)
            return redirect('user')
        elif request.method == 'GET':
            return render(request=request, template_name= 'change_password.html')
    else:
        return redirect('login')
    

def register_user(request: Request):
    if request.method == 'POST':
        byte_data = request.body
        data = json.loads(byte_data.decode("utf-8"))
        username = data["username"]
        password = data["password"]
        email = data["email"]
        auth_user = User.objects.filter(username= username, email= email)
        if auth_user.exists():
            return render(request=request, template_name='login.html')
        else:
            new_user = User.objects.create_user(username=username, password=password, email=email)
            new_user.save()
            login(request=request, user= new_user)
            return redirect('/user')
    elif request.method == 'GET':
        return render(request=request, template_name= 'register.html')
    
def show_main_page(request):
    return render(request=request, template_name= 'main_page.html')