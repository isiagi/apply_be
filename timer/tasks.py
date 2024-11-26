from celery import shared_task

@shared_task
def your_scheduled_task():
    """Task to run every 14 minutes"""
    print("Running scheduled task...")
    # Add your task logic here
    pass