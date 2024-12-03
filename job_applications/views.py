from rest_framework import viewsets
from .models import JobApplication
from .serializers import JobApplicationSerializer
from rest_framework.permissions import IsAuthenticated
from job_listings.models import Job
from rest_framework import serializers

class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        try:
            job_id = self.request.data.get('job')
            job = Job.objects.get(id=job_id)
            serializer.save(applicant=self.request.user, job=job)
        except Job.DoesNotExist:
            raise serializers.ValidationError("Invalid job ID")

    def get_queryset(self):
        # If user is a superuser, show all applications
        if self.request.user.is_superuser:
            return JobApplication.objects.all()
        
        # If user is an employer, show applications for their jobs
        if self.request.user.is_employer:
            # Filter job applications where the job's recruiter matches the current user
            return JobApplication.objects.filter(job__recuiter_id=self.request.user.id)
        
        # If user is an applicant, show only their own applications
        return JobApplication.objects.filter(applicant=self.request.user)