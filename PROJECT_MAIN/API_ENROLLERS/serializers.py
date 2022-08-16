from rest_framework import serializers
from django.db.models.base import Model
from django.db.models import fields
from CAPTURERS.models import Enrollers, Markers
from SERVICES.models import registro
from drf_extra_fields.fields import Base64ImageField

class EnrollersSerializers(serializers.ModelSerializer):
    image_enrollers = Base64ImageField(required=False)
    class Meta:
        model = Enrollers
        fields = '__all__'
        
class MarkersSerializers(serializers.ModelSerializer):
    image_markers = Base64ImageField(required=False)
    class Meta:
        model = Markers
        fields = '__all__'

class RegistrosSerializers(serializers.ModelSerializer):
    class Meta:
        model = registro
        fields = '__all__'