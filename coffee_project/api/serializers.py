from rest_framework import serializers
from .models import CoffeeMachine, CoffeePod

class CoffeeMachineSerializer(serializers.ModelSerializer):
    '''
        Serializer Class to serializer Coffee machine objects to JSON
    '''

    class Meta:
        model = CoffeeMachine
        exclude = ('id',)

class CoffeePodSerializer(serializers.ModelSerializer):
    '''
        Serializer Class to serialize Coffee pods objects to JSON
    '''
    
    class Meta:
        model = CoffeePod
        exclude = ('id',)