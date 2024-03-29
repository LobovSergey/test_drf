from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'description',
                    'image',
                    'date']
    search_fields = (
        'title',
    )
    list_filter = ('title',)
