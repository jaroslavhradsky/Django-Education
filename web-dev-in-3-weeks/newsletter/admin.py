from django.contrib import admin
from .models import Subscriber


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    fields = ["email", "name"]
    list_display = ["email", "name"]
    search_fields = ["email"]
