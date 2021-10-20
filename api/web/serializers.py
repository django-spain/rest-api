from django.forms import fields
from rest_framework import serializers
from .models import Persona

class PersonaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__' 