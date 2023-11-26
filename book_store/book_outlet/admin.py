from django.contrib import admin
from .models import Book, Author, Address, Country

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    #readonly_fields = ('slug',)
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('rating','author')
    list_display = ('title','author')

class AddressAdmin(admin.ModelAdmin):
    pass

admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Address, AddressAdmin)
admin.site.register(Country)
