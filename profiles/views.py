from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import EmployerProfile, ApplicantProfile
from .serializers import (
    EmployerProfileSerializer,
    ApplicantProfileSerializer
)

class UserProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.request.user.is_employer:
            return EmployerProfileSerializer
        return ApplicantProfileSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_employer:
            return EmployerProfile.objects.filter(user=user)
        return ApplicantProfile.objects.filter(user=user)

    @action(detail=False, methods=['POST'])
    def upload_image(self, request):
        user = request.user
        if not request.FILES.get('image'):
            return Response(
                {'error': 'No image provided'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if user.is_employer:
            profile = user.employer_profile
            field_name = 'company_logo'
        else:
            profile = user.applicant_profile
            field_name = 'profile_image'

        serializer = self.get_serializer(
            profile,
            data={field_name: request.FILES['image']},
            partial=True
        )

        if serializer.is_valid():
            # Delete old image if it exists
            old_image = getattr(profile, field_name)
            if old_image:
                old_image.delete(save=False)
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['POST'])
    def upload_resume(self, request):
        user = request.user
        if not user.is_applicant:
            return Response(
                {'error': 'Only applicants can upload resumes'},
                status=status.HTTP_403_FORBIDDEN
            )

        if not request.FILES.get('resume'):
            return Response(
                {'error': 'No resume provided'},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.get_serializer(
            user.applicant_profile,
            data={'resume': request.FILES['resume']},
            partial=True
        )

        if serializer.is_valid():
            if user.applicant_profile.resume:
                user.applicant_profile.resume.delete(save=False)
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
