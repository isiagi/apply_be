from rest_framework import routers
from django.urls import path
from . import views

router = routers.DefaultRouter()
router.register('educations', views.EducationViewSet)

urlpatterns = router.urls