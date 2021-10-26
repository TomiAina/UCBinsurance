from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('counter', views.counter, name='counter'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('pricing', views.pricing, name='pricing'),
    path('services', views.services, name='services'),
    path('index2', views.index, name='index'),
    path('team', views.team, name='team'),
    path('about', views.about, name='about'),
    path('ytb', views.ytb, name='ytb'),
    path('Subscriber', views.Subscriber)
]
#connect to views

#start by creating a url i.e connecting to views
#create a function in views
