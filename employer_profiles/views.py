from rest_framework import viewsets
from .models import EmployerProfile
from .serializers import EmployerProfileSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

# Create your views here.
class EmployerProfileViewSet(viewsets.ModelViewSet):
    queryset = EmployerProfile.objects.all()
    serializer_class = EmployerProfileSerializer
    permission_classes = [IsAuthenticated]

    # Get the currently authenticated user
    def get_queryset(self):
        return EmployerProfile.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Only user employers can create employer profiles
        if not self.request.user.is_employer:
            raise PermissionDenied("Only employers can create employer profiles.")
        # Set the user field to the currently authenticated user
        serializer.save(user=self.request.user)

    