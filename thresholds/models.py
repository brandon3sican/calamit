from django.db import models
from parameters.models import Parameter

# Create your models here.
class Threshold(models.Model):
    parameter = models.ForeignKey(Parameter, on_delete=models.RESTRICT)
    upper_limit = models.DecimalField(max_digits=10, decimal_places=2)
    lower_limit = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)