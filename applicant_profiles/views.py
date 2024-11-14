from rest_framework import viewsets
from .models import ApplicantProfile

# Create your views here.

class ApplicantProfileViewSet(viewsets.ModelViewSet):
    queryset = ApplicantProfile.objects.all()
    serializer_class = ApplicantProfile
