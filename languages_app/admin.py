from django.contrib import admin
from .models import Language

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name', 'year_created', 'main_application_area', 'view_count', 'last_viewed']
    list_filter = ['main_application_area']
    search_fields = ['name', 'description']
    readonly_fields = ['view_count', 'last_viewed']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'logo', 'description', 'year_created')
        }),
        ('Categorization', {
            'fields': ('main_application_area',)
        }),
        ('Popularity Statistics', {
            'fields': ('view_count', 'last_viewed'),
            'description': 'Automatically updated when users view language pages'
        }),
    )