from django.shortcuts import render, redirect
from .models import Feature
from .models import Subscribe
from django.contrib.auth.models import User, auth
from django.contrib import messages
import urllib.request
import urllib
from django.http import HttpResponse


# Create your views here.



def counter(request):
 text = request.POST['text']
 amount_of_words = len(text.split())
 return render(request, 'counter.html', {'amount':amount_of_words})

def portfolio(request):
    return render(request, 'portfolio.html',)


def pricing(request):
    return render(request, 'pricing.html',)

def index22(request):
    return render(request, 'index22.html',)

def services(request):
    return render(request, 'services.html',)

def about(request):
    return render(request, 'about.html',)

def team(request):
    return render(request, 'team.html',)

def index(request) :
    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features})

def Subscriber(request):
    subscription = Subscribe()
    return render(request, 'index.html', {'subscription': subscription})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid information')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Exists')
                return redirect(register)
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Exists')
                return redirect(register)
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save();
                return redirect(login)
        else:
            messages.info(request, 'Password Incorrect')
            return redirect(register)
    else:
        return render(request, 'register.html')









 # feature1 = Feature()
    # feature1.id = 0
    # feature1.name = 'fast'
    # feature1.details = 'our service is very fast'
    #
    # feature2 = Feature()
    # feature2.id = 1
    # feature2.name = 'reliable'
    # feature2.details = 'our service is very reliable'
    #
    # feature3 = Feature()
    # feature3.id = 2
    # feature3.name = 'affordable'
    # feature3.details = 'our service is very affordable'
    #
    # feature4 = Feature()
    # feature4.id = 3
    # feature4.name = 'trust'
    # feature4.details = 'our service is trust worthy'
    #
    # features = [feature1, feature2, feature3, feature4]

def ytb(request):
    return urllib.urlopen('http://example.com')