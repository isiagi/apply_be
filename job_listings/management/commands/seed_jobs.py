# jobs/management/commands/seed_jobs.py
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from job_listings.models import Job  # Adjust import based on your model location
from decimal import Decimal

class Command(BaseCommand):
    help = 'Seed the database with job listings'

    def handle(self, *args, **kwargs):
        # Clear existing jobs to prevent duplicates
        Job.objects.all().delete()

        # Jobs data (from previous response)
        jobs_data = [
    # White Collar Jobs
    {
        'title': 'Senior Software Engineer',
        'company': 'TechInnovate Solutions',
        'recuiter_id': 1,
        'description': 'Seeking a talented software engineer to develop cutting-edge web applications.',
        'location': 'San Francisco, CA',
        'salary': 145000.00,
        'experience_level': 'Senior',
        'contact_email': 'careers@techinnovate.com',
        'job_type': 'White'
    },
    {
        'title': 'Marketing Director',
        'company': 'Global Brands Inc.',
        'recuiter_id': 1,
        'description': 'Lead our marketing strategy and drive brand growth across multiple channels.',
        'location': 'New York, NY',
        'salary': 135000.00,
        'experience_level': 'Executive',
        'contact_email': 'jobs@globalbrandsinc.com',
        'job_type': 'White'
    },
    {
        'title': 'Financial Analyst',
        'company': 'Quantum Investment Group',
        'recuiter_id': 1,
        'description': 'Perform financial modeling and provide strategic investment recommendations.',
        'location': 'Chicago, IL',
        'salary': 95000.00,
        'experience_level': 'Mid-Level',
        'contact_email': 'recruiting@quantumgroup.com',
        'job_type': 'White'
    },
    {
        'title': 'HR Business Partner',
        'company': 'People First Consulting',
        'recuiter_id': 1,
        'description': 'Develop and implement HR strategies to support organizational growth.',
        'location': 'Boston, MA',
        'salary': 110000.00,
        'experience_level': 'Senior',
        'contact_email': 'careers@peoplefirst.com',
        'job_type': 'White'
    },
    {
        'title': 'Data Science Manager',
        'company': 'AI Innovations LLC',
        'recuiter_id': 1,
        'description': 'Lead a team of data scientists in developing machine learning solutions.',
        'location': 'Seattle, WA',
        'salary': 165000.00,
        'experience_level': 'Executive',
        'contact_email': 'talent@aiinnovations.com',
        'job_type': 'White'
    },
    
    # Blue Collar Jobs
    {
        'title': 'Skilled Electrician',
        'company': 'Power Systems Electrical',
        'recuiter_id': 1,
        'description': 'Experienced electrician needed for commercial and residential projects.',
        'location': 'Houston, TX',
        'salary': 65000.00,
        'experience_level': 'Journeyman',
        'contact_email': 'hiring@powersystems.com',
        'job_type': 'Blue'
    },
    {
        'title': 'Truck Driver',
        'company': 'National Logistics Transport',
        'recuiter_id': 1,
        'description': 'Class A CDL drivers needed for long-haul interstate routes.',
        'location': 'Denver, CO',
        'salary': 58000.00,
        'experience_level': 'Experienced',
        'contact_email': 'drivers@nationaltransport.com',
        'job_type': 'Blue'
    },
    {
        'title': 'Welding Technician',
        'company': 'MetalCraft Manufacturing',
        'recuiter_id': 1,
        'description': 'Skilled welder for industrial manufacturing with certification required.',
        'location': 'Detroit, MI',
        'salary': 62000.00,
        'experience_level': 'Senior',
        'contact_email': 'careers@metalcraft.com',
        'job_type': 'Blue'
    },
    {
        'title': 'Construction Foreman',
        'company': 'BuildRight Construction',
        'recuiter_id': 1,
        'description': 'Oversee construction site operations and manage construction teams.',
        'location': 'Phoenix, AZ',
        'salary': 72000.00,
        'experience_level': 'Senior',
        'contact_email': 'jobs@buildrightconstruction.com',
        'job_type': 'Blue'
    },
    {
        'title': 'HVAC Technician',
        'company': 'Climate Control Experts',
        'recuiter_id': 1,
        'description': 'Install and repair heating, ventilation, and air conditioning systems.',
        'location': 'Atlanta, GA',
        'salary': 55000.00,
        'experience_level': 'Intermediate',
        'contact_email': 'careers@climatecontrol.com',
        'job_type': 'Blue'
    }
]


        # Create jobs
        created_jobs = []
        for job_info in jobs_data:
            job = Job.objects.create(
                title=job_info['title'],
                company=job_info['company'],
                description=job_info['description'],
                location=job_info['location'],
                salary=Decimal(str(job_info['salary'])),  # Convert to Decimal
                experience_level=job_info['experience_level'],
                contact_email=job_info['contact_email'],
                job_type=job_info['job_type'],
                # Assuming recuiter_id is optional or you have a way to link it
                recuiter_id_id=job_info.get('recuiter_id')
            )
            created_jobs.append(job)

        self.stdout.write(self.style.SUCCESS(f'Successfully created {len(created_jobs)} job listings'))