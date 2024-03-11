from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email',
                    'password',
                    'phone',
                    'organizations']

    search_fields = (
        'email', 'phone',
    )
