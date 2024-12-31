# profiles/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import EmployerProfile, ApplicantProfile

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal handler to create appropriate profile when a new user is created
    """
    if created:
        if instance.is_employer:
            EmployerProfile.objects.create(
                user=instance,
                company_name="",
                company_description="",
                industry="",
                company_size="",
                website="",
                location=""
            )
        elif instance.is_applicant:
            ApplicantProfile.objects.create(
                user=instance,
                bio="",
                skills=[],
                education=[],
                experience_years=0,
                current_position="",
                location=""
            )

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    """
    Signal handler to save profile changes when user is updated
    """
    if instance.is_employer and hasattr(instance, 'employer_profile'):
        instance.employer_profile.save()
    elif instance.is_applicant and hasattr(instance, 'applicant_profile'):
        instance.applicant_profile.save()