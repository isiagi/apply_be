from rest_framework import serializers
from .models import EmploymentHistory

class EmploymentHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmploymentHistory
        fields = '__all__'