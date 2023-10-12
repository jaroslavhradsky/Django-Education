from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

music = [
    {
        'id': 0,
        'name': 'The Wall',
        'interpret': 'Pink Floyd'
    },
    {
        'id': 1,
        'name': 'A Night at the Opera',
        'interpret': 'Queen'
    },
    {
        'id': 2,
        'name': 'The Division Bell',
        'interpret': 'Pink Floyd'
    },
    {
        'id': 3,
        'name': 'Die goldene Stimme aus Prag',
        'interpret': 'Karel Gott'
    },
]

def list(request):
    return render(request, 'catalog/list.html', {
        'music': music,
    })

def album(request, id):
    return render(request, 'catalog/album.html', {
        'name': music[id]['name'],
        'interpret': music[id]['interpret'],
    })
