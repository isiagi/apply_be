from rest_framework import viewsets
from .models import ApplicantProfile
from .serializers import ApplicantProfileSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class ApplicantProfileViewSet(viewsets.ModelViewSet):
    queryset = ApplicantProfile.objects.all()
    serializer_class = ApplicantProfileSerializer
    permission_classes = [IsAuthenticated]

    # Get the current user's profile
    def get_queryset(self):
        return ApplicantProfile.objects.filter(user=self.request.user)
