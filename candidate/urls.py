from django.urls import path, include
from rest_framework import routers
from .views import CandidateViewSet

router = routers.SimpleRouter()
router.register('candidate', CandidateViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
