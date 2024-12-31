from django.db import models

class Education(models.Model):
    profile = models.ForeignKey('profiles.ApplicantProfile', on_delete=models.CASCADE, related_name='education_entries', null=True, blank=True)
    institution = models.CharField(max_length=255, blank=True, null=True)
    degree = models.CharField(max_length=255, blank=True, null=True)
    field_of_study = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    current = models.BooleanField(default=False, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-end_date', '-start_date']
        verbose_name = 'Education Entry'
        verbose_name_plural = 'Education Entries'

    def __str__(self):
        return f"{self.degree} in {self.field_of_study} at {self.institution}"