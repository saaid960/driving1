from django.shortcuts import render, redirect
from . models import messages



def home(request):
    return render(request, "home/home.html")


def Applypage(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        context = messages(name=name,number=number)
        context.save()
    return render(request, "home/Apply.html")

def contactpage(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        context = messages(name=name,number=number)
        context.save()
    return redirect('home/Apply.html')
