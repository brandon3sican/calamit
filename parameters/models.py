from django.db import models

# Create your models here.
class Parameter(models.Model):
    parameter_name = models.CharField(max_length=100)
    description = models.TextField()
    measurement_unit = models.CharField(max_length=30)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)