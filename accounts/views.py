from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from accounts.models import *


def register_view(request):
    
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        
        user=User()
        insight=create_insight()
        
        user.username=request.POST.get('username')
        user.password=request.POST.get('password')
        user.id_insights=insight
        user.save()
        
        request.session['username'] = request.POST.get('username')
        request.session['password'] = request.POST.get('password')
        
        print(request.session['username'])
        print(request.session['password'])
        
        return redirect('login')

def login_view(request):
    
    if request.method == 'GET':
    
        username=request.session.get('username')
        password= request.session.get('password')
        
        request.session.pop('username', None)
        request.session.pop('password', None)
        
        return render(request, 'login.html', {'username':username, 'password':password})
    
    elif request.method ==  'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        
        if user is not None:
            login(request,user)
            return redirect('random_form')
        else:
            return render(request, 'login.html')
        
    return render(request, 'random_form', {'user':user})
        
        

    
def logout_view(request):
    logout(request)
    return redirect('login')


def create_insight():
   insight= Insights.objects.create(
        errors_count=0,
        hit_count=0
    )
   print(type(insight))
   return insight
