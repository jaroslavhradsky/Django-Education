from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def list(request):
    return HttpResponse('This is a list page')

def album(request):
    return HttpResponse('This is an album page')
