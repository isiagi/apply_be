from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'is_employer', 'is_applicant']


    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.is_employer = validated_data.get('is_employer', instance.is_employer)
        instance.is_applicant = validated_data.get('is_applicant', instance.is_applicant)

        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
            
        instance.save()
        return instance