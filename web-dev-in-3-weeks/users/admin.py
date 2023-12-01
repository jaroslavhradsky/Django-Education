from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = [
        "email",
        "is_active",
        "is_staff",
        "is_superuser",
    ]
    ordering = ["email"]
    fieldsets = [
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {
            'fields': [
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions'
            ],
        }),
        ('Important dates', {'fields': ('last_login',)}),
    ]
