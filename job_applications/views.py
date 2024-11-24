from rest_framework import viewsets
from .models import JobApplication
from .serializers import JobApplicationSerializer
from rest_framework.permissions import IsAuthenticated

class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user)

    def get_queryset(self):
        # Optionally: filter to show only user's own applications
        return JobApplication.objects.filter(applicant=self.request.user)