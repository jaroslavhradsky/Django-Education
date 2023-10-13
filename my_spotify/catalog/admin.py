from django.contrib import admin
from .models import Album

# Register your models here.

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('interpret', 'name', 'image')
    list_filter = ('interpret',)

admin.site.register(Album, AlbumAdmin)
