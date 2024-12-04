from rest_framework import viewsets
from .models import EmploymentHistory
from .serializers import EmploymentHistorySerializer

# Create your views here.
class EmploymentHistoryViewSet(viewsets.ModelViewSet):
    queryset = EmploymentHistory.objects.all()
    serializer_class = EmploymentHistorySerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
