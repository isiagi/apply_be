from rest_framework import viewsets
from .models import JobApplication
from .serializers import JobApplicationSerializer

# Create your views here.

class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
