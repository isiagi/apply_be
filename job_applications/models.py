from django.db import models

# Create your models here.
class JobApplication(models.Model):
    job = models.ForeignKey('job_listings.Job', on_delete=models.CASCADE)
    applicant = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    date_applied = models.DateField(auto_now_add=True)
    application_status = models.CharField(max_length=20, default='applied')


    def __str__(self):
        return f"{self.applicant} - {self.job}"
