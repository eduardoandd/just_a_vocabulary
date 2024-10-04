from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from accounts.forms import RegisterForm
from accounts.models import *
from django.contrib.auth.hashers import check_password


def register_view(request):
    
    if request.method == 'POST':
        new_register_form= RegisterForm(request.POST)
        if new_register_form.is_valid():
            new_register_form.save()
            return redirect('login')
    else:
        register_form=RegisterForm()
    
    return render(request, 'register.html', {'register_form': register_form})
    
    
def authenticate_user(username, password):
    try:
        user = User.objects.get(username=username)
        if check_password(password, user.password): 
            return user
    except User.DoesNotExist:
        return None 

def login_view(request):
    
    if request.method=="POST":
        username= request.POST['username']
        password= request.POST['password']
        user= authenticate_user(username=username, password=password)
        
        if user is not None:
            login(request,user)
            return redirect('random_form')
        else:
            login_form=AuthenticationForm()
    else:
        login_form= AuthenticationForm()
    
    return render(request, 'login.html', {'login_form': login_form})
    
def logout_view(request):
    logout(request)
    return redirect('login')
        