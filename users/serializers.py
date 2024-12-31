from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'is_employer', 'is_applicant', 'first_name', 'last_name']
        extra_kwargs = {
            'password': {'write_only': True},
            'is_employer': {'required': True},
            'is_applicant': {'required': True},
        }

    def validate(self, data):
        # Ensure user can't be both employer and applicant
        if data.get('is_employer') and data.get('is_applicant'):
            raise serializers.ValidationError(
                "User cannot be both employer and applicant"
            )
        # Ensure user must be either employer or applicant
        if not data.get('is_employer') and not data.get('is_applicant'):
            raise serializers.ValidationError(
                "User must be either employer or applicant"
            )
        return data

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = CustomUser.objects.create(**validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)
            
        instance.save()
        return instance
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)