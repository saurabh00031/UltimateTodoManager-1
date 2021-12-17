from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate , login as loginUser , logout
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from app.forms import TODOForm
from app.models import TODO
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


#@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        form = TODOForm()
        todos = TODO.objects.filter(user=request.user.id).order_by('priority')
        return render(request , 'index.html' , {'form' : form , 'todos' : todos})
    else:
        form1 = AuthenticationForm()
        return render(request , 'login.html' ,  {"form" : form1})


def login(request):
    if request.method == 'GET':
        form1 = AuthenticationForm()
        return render(request , 'login.html' , {"form" : form1})
    else:
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username , password = password)
            if user is not None:
                loginUser(request , user)
                return redirect('home')
        else:
            return render(request , 'login.html' ,  {"form" : form})


def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request , 'signup.html' ,{"form" : form})
    else:
        form = UserCreationForm(request.POST)  
        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect('login')
        else:
            return render(request , 'signup.html' ,{"form" : form})


@login_required(login_url='login')
def update(request,id):
    if request.method == 'GET':
        pi=User.objects.get(pk=id)
        form = UserCreationForm(instance=pi)
        return render(request , 'update.html' ,{"form" : form})
    else:
        print(request.POST)
        pi=User.objects.get(pk=id)
        form = UserCreationForm(request.POST,instance=pi)  
        if form.is_valid():
            user = form.save()
            print(user)
            return render(request , 'login.html' ,{"form" : form})
        else:
            return render(request , 'update.html' ,{"form" : form})


@login_required(login_url='login')
def deletes(request,id):
    if request.method=="POST":  
       dlt=User.objects.get(pk=id)
       dlt.delete()
       return redirect('/')


@login_required(login_url='login')
def add_todo(request):
    if request.user.is_authenticated:
       # user = request.user
        print(request.user)
        form = TODOForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            print(todo)
            return redirect("home")
        else: 
            return render(request , 'index.html' ,{'form' : form})


def delete_todo(request , id ):
    TODO.objects.get(pk = id).delete()
    return redirect('home')

def change_todo(request , id  , status):
    todo = TODO.objects.get(pk = id)
    todo.status = status
    todo.save()
    return redirect('home')


def signout(request):
    logout(request)
    return redirect('login')

def about(request):
    return render(request,'about.html')