from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'accounts/dashboard.html')


def signup(request):
    return render(request, 'accounts/signup.html')


def signin(request):
    return render(request, 'accounts/signin.html')


def cal(request):
    return render(request, 'accounts/calendar.html')
