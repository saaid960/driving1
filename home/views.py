from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from . models import *
from django.contrib.auth.forms import UserCreationForm
from .form import createuserform
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . form import *

def home(request):
    return render(request, "home/home.html")

def video(request):
    obj =VIDEO.objects.all()
    return render(request, 'home/Tutorial.html',{'obj':obj})

def contactpage(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        context = messages(name=name,number=number)
        context.save()
    return redirect('home/Apply.html')

def registerpage(request):
    
    form = createuserform()
    if request.method == "POST":
        form = createuserform(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account was created for" + user)
            return redirect("login")
    context = {'form': form}
    return render(request, "home/register.html", context)


def loginpage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.info(request, "username OR password is incorrect")
        
    return render(request, "home/login.html")


def logoutuser(request):
    return redirect("")
    


@login_required(login_url="login")
def index(request):
    todo_items = TodoItem.objects.all()
    l = TaskForm()
    context =  {'todo_items': todo_items, "l": l}
    return render(request, 'home/list.html', context)



def addTodo(request):
    new_post = TodoItem(content = request.POST['content'])
    new_post.save()
    return HttpResponseRedirect('/todo/')

def deleteTodo(request, i_id):
    de = TodoItem.objects.get(id=i_id)
    de.delete()
    return HttpResponseRedirect('/todo/')