from django.shortcuts import render, HttpResponse

# Create your views here.

def indexpage(request):
    return HttpResponse('Welcome')

def aboutpage(request):
    return HttpResponse('You are at About page')