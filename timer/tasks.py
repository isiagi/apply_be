from celery import shared_task
import requests

@shared_task
def your_scheduled_task():
    """Task to run every 14 minutes"""
    print("Running scheduled task...")
    # Add your task logic here
    requests.get('https://apply-be.onrender.com/api/job_listings/jobs/')

    return "Server pinged!"