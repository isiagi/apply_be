from rest_framework import viewsets
from .models import Education
from .serializers import EducationSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
