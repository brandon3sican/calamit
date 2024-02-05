from django.db import models

# Create your models here.
class Factor(models.Model):
    factor_name = models.CharField(max_length=100)
    description = models.TextField()
    short_name = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.factor_name

    class Meta:  
        db_table = "factors"


from django.db import models
from factors.models import Factor

# Create your models here.
class FactorRating(models.Model):
    factor = models.ForeignKey(Factor, on_delete=models.RESTRICT)
    factor_rating_name = models.CharField(max_length=100)
    factor_rating_value = models.DecimalField(max_digits=5, decimal_places=2)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.factor_rating_name

    class Meta:  
        db_table = "factor_ratings"