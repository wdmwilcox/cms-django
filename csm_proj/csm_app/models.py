from django.db import models

class PhoneNumber(models.Model):
    number = models.CharField(max_length=11)
    
    def __str__(self):
        return self.number

class Company(models.Model):
    name = models.CharField(max_length=200)
    phone_numbers = models.ManyToManyField(PhoneNumber)
    
    def __str__(self):
        return self.name
    
class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_numbers = models.ManyToManyField(PhoneNumber)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    


    
