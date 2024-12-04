from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from employer_profiles.models import EmployerProfile
from applicant_profiles.models import ApplicantProfile

# Get the custom user model
User = get_user_model()

@receiver(post_save, sender=User)
def create_employer_profile(sender, instance, created, **kwargs):
    """
    Signal to create an employer profile automatically when an employer user is created.
    
    :param sender: The model class sending the signal (User model)
    :param instance: The actual instance of the User being saved
    :param created: Boolean indicating if this is a new user creation
    """
    # Only create profile if:
    # 1. This is a new user creation
    # 2. The user is marked as an employer
    if created and instance.is_employer:
        EmployerProfile.objects.create(user=instance)
    else:
        ApplicantProfile.objects.create(user=instance)