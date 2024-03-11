from django.contrib import admin
from .models import Organization


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'description',
                    'postcode',
                    'address']

    search_fields = (
        'title', 'postcode',
    )
    list_filter = ('postcode', 'address')
