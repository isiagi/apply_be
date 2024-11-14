# use defaultRouter

from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('jobs', views.JobViewSet)

# urlpatterns = [
#     path('', views.JobViewSet.as_view(), name='job-list'),
#     path('<int:pk>', views.JobViewSet.as_view(), name='job-detail'),
# ]

urlpatterns = router.urls
