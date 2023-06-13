from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

# Create your views here.
def index(request):
    features = Feature.objects.all
    return render(request, 'website/index.html', {'features' : features})

def counter(request):
    words = request.POST['text']
    number_of_words = len(words.split(" "))
    context = {
        "number_of_words": number_of_words
    }
    return render(request, "website/counter.html", context)

def lucy(request):
    return render(request, "website/lucy.html")

def statictest(request):
    return render(request, "website/statictest.html")

def wordcounter(request):
    return render(request, "website/wordcounter.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords Do Not Match')
            return redirect('register')
    else:
        return render(request, "website/register.html")
    
def login(request):
    return render(request, 'website/login.html')