from rest_framework import routers
from django.urls import path
from . import views

router = routers.DefaultRouter()
router.register('profiles', views.ApplicantProfileViewSet)

# urlpatterns = [
#     path('', views.ApplicantProfileViewSet.as_view(), name='profile-list'),
#     path('<int:pk>', views.ApplicantProfileViewSet.as_view(), name='profile-detail'),
# ]

urlpatterns = router.urls