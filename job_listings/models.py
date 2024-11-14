from django.db import models

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    recuiter_id = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(max_length=500)
    location = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    experience_level = models.CharField(max_length=50)
    contact_email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
