from rest_framework import viewsets
from .models import ApplicantProfile
from .serializers import ApplicantProfileSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class ApplicantProfileViewSet(viewsets.ModelViewSet):
    queryset = ApplicantProfile.objects.all()
    serializer_class = ApplicantProfileSerializer
    permission_classes = [IsAuthenticated]

    # Get the current user's profile
    def get_queryset(self):
        return ApplicantProfile.objects.filter(user=self.request.user)
    
    # Update the current user's profile
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    # Delete the current user's profile
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user == request.user:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
