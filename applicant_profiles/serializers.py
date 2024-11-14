from rest_framework import serializers
from .models import ApplicantProfile


class ApplicantProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicantProfile
        fields = '__all__'