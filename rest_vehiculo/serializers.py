from django.db import models
from django.db.models import fields
from rest_framework import serializers
from core.models import Vehiculo

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = ['patente','marca','modelo','categoria']
