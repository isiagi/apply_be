from rest_framework import viewsets
from .models import EmployerProfile
from .serializers import EmployerProfileSerializer

# Create your views here.
class EmployerProfileViewSet(viewsets.ModelViewSet):
    queryset = EmployerProfile.objects.all()
    serializer_class = EmployerProfileSerializer   

    