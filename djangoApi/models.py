from django.db import models

# Measurement Choices
MEASUREMENT_UNIT = (
    ("Kg", "KG"),
    ("Liters", "Ltrs"),
    ("Units", "Units"),
)
# Direction Choices
DIRECTION_UNIT = (
    ("IN", "IN"),
    ("OUT", "OUT"),
)


# Product Model
class Product(models.Model):
    name = models.CharField(max_length=30)
    measurement_unit = models.CharField(max_length=50, choices=MEASUREMENT_UNIT, default='', )


# Operation Model
class Operation(models.Model):
    date = models.DateField()
    direction = models.CharField(default='', choices=DIRECTION_UNIT, max_length=50)
    amount = models.IntegerField(default=0)
