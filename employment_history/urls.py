from rest_framework import routers
from django.urls import path
from . import views

router = routers.DefaultRouter()
router.register('history', views.EmploymentHistoryViewSet)

urlpatterns = router.urls