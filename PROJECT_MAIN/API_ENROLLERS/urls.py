from rest_framework import routers
from API_ENROLLERS.views import *
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'enrolar', EnrollersViewsets, basename= 'enrolar')
router.register(r'registro', RegistroViewsets, basename= 'registro')
router.register(r'marcadores', MarkerViewsets, basename= 'marcadores')

urlpatterns = [
    path('api/', include(router.urls)),
]