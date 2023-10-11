from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

music = [
    {
        'name': 'The Wall',
        'interpret': 'Pink Floyd'
    },
    {
        'name': 'A Night at the Opera',
        'interpret': 'Queen'
    },
    {
        'name': 'The Division Bell',
        'interpret': 'Pink Floyd'
    },
    {
        'name': 'Die goldene Stimme aus Prag',
        'interpret': 'Karel Gott'
    },
]

def list(request):
    return HttpResponse('This is a list page')

def album(request, id):
    response = 'this is <strong>' + music[id]['name'] + '</strong> album by ' + music[id]['interpret']
    print(response)
    return HttpResponse(response)
