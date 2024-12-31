from django.shortcuts import render
from job_listings.models import Job
from job_listings.serializers import JobSerializer
from rest_framework import viewsets

# authorization
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]
    # Get id of user when creating a job and insert into job object

    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(recuiter_id=self.request.user)

    # Get id of user when updating a job and insert into job object

    def perform_update(self, serializer):
        serializer.save(recuiter_id=self.request.user)
