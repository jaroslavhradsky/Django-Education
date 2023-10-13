from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Album

# Create your views here.

music = Album.objects.all().order_by('interpret')

def list(request):
    return render(request, 'catalog/list.html', {
        'music': music,
    })

def album(request, id):
    album = Album.objects.get(pk=id)
    return render(request, 'catalog/album.html', {
        'name': album.name,
        'interpret': album.interpret,
        'image': album.image,
    })
