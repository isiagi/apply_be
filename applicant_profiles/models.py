from django.db import models


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

# Create your models here.
class ApplicantProfile(models.Model):
    resume_url = models.URLField(null=True, blank=True)
    linkedin_url = models.URLField(null=True, blank=True)
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, null=True, blank=True)
    portfolio_url = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_to, null=True, blank=True)
    skills = models.TextField(max_length=500, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)  # Guaranteed to always return a string
