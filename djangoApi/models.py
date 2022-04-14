from django.db import models

# Create your models here.
MEASUREMENT_UNIT = (
    ("Kg", "KG"),
    ("Liters", "Ltrs"),
    ("Units", "Units"),
)
DIRECTION_UNIT = (
    ("IN", "IN"),
    ("OUT", "OUT"),
)


class Product(models.Model):
    name = models.CharField(max_length=30)
    measurement_unit = models.CharField(max_length=50, choices=MEASUREMENT_UNIT, default='', )


class Operation(models.Model):
    date = models.DateField()
    direction = models.CharField(default='', choices=DIRECTION_UNIT, max_length=50)
    amount = models.IntegerField(default=0)
