from rest_framework import serializers
from .models import Job
from users.models import CustomUser  # Assuming CustomUser is in the users app

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name']  # Explicitly include safe fields

class JobSerializer(serializers.ModelSerializer):
    # recuiter_id = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), required=True)
    recuiter_details = CustomUserSerializer(source='recuiter_id', read_only=True)  # Include recruiter details in response

    class Meta:
        model = Job
        fields = '__all__'
