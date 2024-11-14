from rest_framework import routers
from django.urls import path
from . import views

router = routers.DefaultRouter()
router.register('applications', views.JobApplicationViewSet)

# urlpatterns = [
#     path('', views.JobApplicationViewSet.as_view(), name='application-list'),
#     path('<int:pk>', views.JobApplicationViewSet.as_view(), name='application-detail'),
# ]

urlpatterns = router.urls