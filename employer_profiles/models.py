from django.db import models

# Create your models here.
class EmployerProfile(models.Model):
    company_name = models.CharField(max_length=100)
    company_description = models.TextField()
    industry = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, null=True, blank=True)
    contact_email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name
