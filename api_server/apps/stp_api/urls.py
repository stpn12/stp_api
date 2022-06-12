from rest_framework import routers
from .api import SpeechApiViewSet
from django.urls import include
from . import views


# структура url
router = routers.DefaultRouter()
router.register('api/stp_api',  SpeechApiViewSet, 'stp_api')

app_name = "stp_api"
urlpatterns = router.urls
