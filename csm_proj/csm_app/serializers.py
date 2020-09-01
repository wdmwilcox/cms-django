from rest_framework import serializers
from .models import Company, Person, PhoneNumber

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'phone_number',]
        
class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'phone_number',]
        

        
       