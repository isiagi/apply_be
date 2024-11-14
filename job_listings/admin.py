from django.contrib import admin

# Register your models here.

from job_listings.models import Job

admin.site.register(Job)
