from django.shortcuts import render
from job_listings.models import Job
from job_listings.serializers import JobSerializer
from rest_framework import viewsets


# Create your views here.

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
