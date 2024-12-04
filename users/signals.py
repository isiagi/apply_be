from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from employer_profiles.models import EmployerProfile
from applicant_profiles.models import ApplicantProfile
from employment_history.models import EmploymentHistory
from education.models import Education

# Get the custom user model
User = get_user_model()

@receiver(post_save, sender=User)
def create_user_profiles(sender, instance, created, **kwargs):
    """
    Signal to create profiles automatically based on user type.
    
    :param sender: The model class sending the signal (User model)
    :param instance: The actual instance of the User being saved
    :param created: Boolean indicating if this is a new user creation
    """
    # Only create profiles if this is a new user creation
    if created:
        # If user is an employer, create employer profile
        if instance.is_employer:
            print("Creating Employer Profile", instance)
            EmployerProfile.objects.create(user=instance)
        
        # If user is an applicant, create applicant profile
        elif instance.is_applicant:
            print("Creating Applicant Profile", instance)
            ApplicantProfile.objects.create(user=instance)
            EmploymentHistory.objects.create(user=instance)
            Education.objects.create(user=instance)
    