from django.contrib import admin

from .models import Education


class EducationInline(admin.StackedInline):
    model = Education
    extra = 0
    fields = ('institution', 'degree', 'field_of_study', 'start_date', 
              'end_date', 'current', 'description')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('profile', 'degree', 'institution', 'field_of_study', 
                   'start_date', 'end_date', 'current')
    list_filter = ('degree', 'current')
    search_fields = ('institution', 'degree', 'field_of_study', 
                    'profile__user__username')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('profile', 'institution', 'degree', 'field_of_study')
        }),
        ('Timeline', {
            'fields': ('start_date', 'end_date', 'current')
        }),
        ('Additional Information', {
            'fields': ('description',)
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )