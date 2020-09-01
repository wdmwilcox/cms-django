from django.shortcuts import render
from rest_framework import viewsets
from .models import Company, Person
from .serializers import CompanySerializer, PersonSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer




    
