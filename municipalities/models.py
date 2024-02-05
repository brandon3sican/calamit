from django.db import models

# Create your models here.
class Municipality(models.Model):
    municipality_name = models.CharField(max_length=100)
    description =  models.TextField()
    contact_person = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=11)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.municipality_name
        
    class Meta:
        db_table = 'municipalities'
