from rest_framework import serializers
from django.contrib.auth import get_user_model
from education.serializers import EducationSerializer
from .models import EmployerProfile, ApplicantProfile

User = get_user_model()

class UserLimitedSerializer(serializers.ModelSerializer):
    """Serializer for User model with limited fields"""
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')
        read_only_fields = ('id', 'username', 'email')  # These can't be edited through profile


class EmployerProfileSerializer(serializers.ModelSerializer):
    user = UserLimitedSerializer()
    class Meta:
        model = EmployerProfile
        fields = ('company_name', 'user', 'company_description', 'industry', 'company_size',
                 'company_logo', 'website', 'location', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')

    def validate_company_logo(self, value):
        if value and value.size > 2 * 1024 * 1024:  # 2MB limit
            raise serializers.ValidationError("Logo size should not exceed 2MB")
        return value
    
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        
        # Update user data if provided
        if user_data:
            user = instance.user
            # Only update allowed fields
            user.first_name = user_data.get('first_name', user.first_name)
            user.last_name = user_data.get('last_name', user.last_name)
            user.save()

        # Update profile data
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance

class ApplicantProfileSerializer(serializers.ModelSerializer):
    user = UserLimitedSerializer()
    education_entries = EducationSerializer(many=True, read_only=True)
    class Meta:
        model = ApplicantProfile
        fields = ('profile_image', 'user', 'bio', 'skills', 'experience_years', 'education_entries',
                 'resume', 'current_position', 'location', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')

    def validate_profile_image(self, value):
        if value and value.size > 2 * 1024 * 1024:  # 2MB limit
            raise serializers.ValidationError("Image size should not exceed 2MB")
        return value

    def validate_resume(self, value):
        if value and value.size > 5 * 1024 * 1024:  # 5MB limit
            raise serializers.ValidationError("Resume size should not exceed 5MB")
        return value
    
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        
        # Update user data if provided
        if user_data:
            user = instance.user
            # Only update allowed fields
            user.first_name = user_data.get('first_name', user.first_name)
            user.last_name = user_data.get('last_name', user.last_name)
            user.save()

        # Update profile data
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance
