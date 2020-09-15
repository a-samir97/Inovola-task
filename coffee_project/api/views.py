from django_filters import rest_framework as filters

from rest_framework.generics import ListAPIView

from .models import CoffeePod, CoffeeMachine
from .serializers import CoffeeMachineSerializer, CoffeePodSerializer

class AllCoffeeMachines(ListAPIView):
    '''
        A class that returns single or list of serialized objects of Coffee Machines 
    '''
    
    queryset = CoffeeMachine.objects.all()
    serializer_class = CoffeeMachineSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ('product_type', 'product_model', 'water_line_compatible')

class AllCoffeePods(ListAPIView):
    '''
        A class that returns single or list of serialized objects of Coffee Pods
    '''

    queryset = CoffeePod.objects.all()
    serializer_class = CoffeePodSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ('product_type', 'coffee_flavor', 'pack_size')