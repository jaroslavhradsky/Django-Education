from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def monthly_challenge(request, month):
    if month == 'january': return HttpResponse('Eat no meat for the entire month')
    elif month == 'february': return HttpResponse('Walk for 20 minutes every day')
    elif month == 'march': return HttpResponse('Lear Django for 20 minutes every day')
    return HttpResponseNotFound('HttpResponseNotFound: This month is not supported!')