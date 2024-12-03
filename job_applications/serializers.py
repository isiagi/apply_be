from rest_framework import serializers
from .models import JobApplication
from job_listings.models import Job

class JobApplicationSerializer(serializers.ModelSerializer):
    # job = serializers.PrimaryKeyRelatedField(queryset=Job.objects.all())
    # applicant = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = JobApplication
        fields = '__all__'

        depth = 1