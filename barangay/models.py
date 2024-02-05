from django.db import models
from municipalities.models import Municipality

# Create your models here.
class Barangay(models.Model):
    barangay_name = models.CharField(max_length=100)
    municipality = models.ForeignKey(Municipality, on_delete=models.RESTRICT)
    description =  models.TextField()
    contact_person = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=11)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.barangay_name

    class Meta:
        db_table = 'barangays'