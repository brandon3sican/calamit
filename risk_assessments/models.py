from django.db import models
from barangay.models import Barangay
from factors.models import FactorRating

# Create your models here.
class RiskAssessment(models.Model):
    barangay = models.ForeignKey(Barangay, on_delete=models.RESTRICT)
    landmark = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=8, decimal_places=5)
    longitude = models.DecimalField(max_digits=8, decimal_places=5)
    elevation = models.DecimalField(max_digits=10, decimal_places=2)

    vFactor = models.ForeignKey(FactorRating, on_delete=models.RESTRICT, related_name = "vegetation", db_column='vFactor') #vegetation
    fFactor = models.ForeignKey(FactorRating, on_delete=models.RESTRICT, related_name = "failure", db_column='fFactor') #failure
    sRed = models.ForeignKey(FactorRating, on_delete=models.RESTRICT, related_name = "spring", db_column='sRed') #spring
    dRed = models.ForeignKey(FactorRating, on_delete=models.RESTRICT, related_name = "drainage", db_column='dRed') #drainage
    lFactor = models.ForeignKey(FactorRating, on_delete=models.RESTRICT, related_name = "land_use", db_column='lFactor') #land_use
    sRating = models.ForeignKey(FactorRating, on_delete=models.RESTRICT, related_name = "soil_mass", db_column='sRating') #soil_mass
    aRating = models.ForeignKey(FactorRating, on_delete=models.RESTRICT, related_name = "slope", db_column='aRating') #slope
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.landmark

    class Meta:  
        db_table = "risk_assessment"