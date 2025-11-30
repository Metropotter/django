from django.contrib import admin
from .models import Language, SiteVisitor, UserProfile, Question, Answer, Comment 

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

@admin.register(SiteVisitor)
class SiteVisitorAdmin(admin.ModelAdmin):
    list_display = ['total_visitors', 'last_updated']
    readonly_fields = ['total_visitors', 'last_updated']
    
    def has_add_permission(self, request):
        return False  # Prevent creating multiple instances
    
    def has_delete_permission(self, request, obj=None):
        return False  # Prevent deletion

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'email_verified']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'content']

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['question', 'mentor', 'answered_at']
    list_filter = ['answered_at']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['question', 'user', 'created_at']
    list_filter = ['created_at']