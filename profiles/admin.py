from django.contrib import admin
from .models import EmployerProfile, ApplicantProfile

@admin.register(EmployerProfile)
class EmployerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'company_name', 'industry', 'location', 'created_at')
    list_filter = ('industry', 'company_size')
    search_fields = ('user__username', 'user__email', 'company_name', 'industry', 'location')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Company Information', {
            'fields': (
                'user',
                'company_name',
                'company_description',
                'industry',
                'company_size',
                'location',
                'website'
            )
        }),
        ('Media', {
            'fields': ('company_logo',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
        }),
    )

@admin.register(ApplicantProfile)
class ApplicantProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'current_position', 'experience_years', 'location', 'created_at')
    list_filter = ('experience_years',)
    search_fields = ('user__username', 'user__email', 'current_position', 'location')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Personal Information', {
            'fields': (
                'user',
                'bio',
                'current_position',
                'location',
                'experience_years'
            )
        }),
        ('Professional Details', {
            'fields': ('skills', 'education')
        }),
        ('Documents', {
            'fields': ('profile_image', 'resume')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
        }),
    )

    def get_skills(self, obj):
        return ", ".join(obj.skills) if obj.skills else ""
    get_skills.short_description = 'Skills'