from rest_framework import routers
from .views import LoginView, SignupView
from django.urls import path, include

router = routers.DefaultRouter()
router.register('login', LoginView)
router.register('signup', SignupView, basename='signup')

# urlpatterns = [
#     path('', include(router.urls)),
# ]

urlpatterns = router.urls



