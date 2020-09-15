from django.db import models

class CoffeeMachine(models.Model):
    
    '''
        Coffee Machine Model

        fields :
            - product_code
            - product_type
            - product_model
            - water_line_compatible

    '''

    COFFEE_MACHINE_LARGE = 'CML'
    COFFEE_MACHINE_SMALL = 'CMS'
    ESPRESSO_MACHINE = 'EM'

    COFFEE_MACHINES_PRODUCT_TYPE_CHOICES = (
        (COFFEE_MACHINE_LARGE, 'large machine'),
        (COFFEE_MACHINE_SMALL, 'small machine'),
        (ESPRESSO_MACHINE, 'espresso machine')
    )

    BASE_MODEL = 'B'
    PREMIUM_MODEL = 'P'
    DELUXE_MODEL = 'D'

    COFFEE_MODELS_TYPES_CHOICES = (
        (BASE_MODEL, 'base model'),
        (PREMIUM_MODEL, 'premium model'),
        (DELUXE_MODEL, 'deluxe model')
    )
    
    
    product_code = models.CharField(max_length=10)
    product_model = models.CharField(max_length=1, choices=COFFEE_MODELS_TYPES_CHOICES, default=BASE_MODEL) 
    product_type = models.CharField(max_length=3, choices=COFFEE_MACHINES_PRODUCT_TYPE_CHOICES)
    water_line_compatible = models.BooleanField(default=False)



    def __str__(self):
        return self.product_code

class CoffeePod(models.Model):
    
    '''
        Coffee Pod Model
        fields :
            - product_code
            - product_type
            - coffee_flavor
            - pack_size
    '''
    
    COFFEE_POD_SMALL = 'CPS'
    COFFEE_POD_LARGE = 'CPL'
    ESPRESSO_POD = 'EP'
    
    COFFEE_PODS_PRODUCT_TYPE_CHOICES = (
        (COFFEE_POD_LARGE, 'large coffee pod'),
        (COFFEE_POD_SMALL, 'small coffee pod'),
        (ESPRESSO_POD, 'espresso pod')
    )

    COFFEE_FLAVOR_VANILLA = 'VA'
    COFFEE_FLAVOR_CARAMEL = 'CA'
    COFFEE_FLAVOR_PSL = 'PS'
    COFFEE_FLAVOR_MOCHA = 'MO'
    COFFEE_FLAVOR_HAZELNUT = 'HA'

    COFFEE_FLAVOR_CHOIES = (
        (COFFEE_FLAVOR_VANILLA, 'Vanilla'),
        (COFFEE_FLAVOR_CARAMEL, 'Caramel'),
        (COFFEE_FLAVOR_PSL, 'Psl'),
        (COFFEE_FLAVOR_MOCHA, 'Mocha'),
        (COFFEE_FLAVOR_HAZELNUT, 'Hazelnut')
    )

    DOZEN_1 = '1'
    DOZEN_3 = '3'
    DOZEN_5 = '5'
    DOZEN_7 = '7'

    PACK_SIZE_CHOICES = (
        (DOZEN_1, '1 dozen (12)'),
        (DOZEN_3, '3 dozen (36)'),
        (DOZEN_5, '5 dozen (60)'),
        (DOZEN_7, '7 dozen (84)')
    )

    product_code = models.CharField(max_length=10)
    product_type = models.CharField(max_length=3, choices=COFFEE_PODS_PRODUCT_TYPE_CHOICES)
    coffee_flavor = models.CharField(max_length=2, choices=COFFEE_FLAVOR_CHOIES)
    pack_size = models.CharField(max_length=1, choices=PACK_SIZE_CHOICES)


    def __str__(self):
        return self.product_code
    