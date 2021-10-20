from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.

from .models import Persona
from .serializers import PersonaSerializers

class PersonaViewsets(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializers

