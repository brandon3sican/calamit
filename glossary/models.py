from django.db import models

# Create your models here.
class Glossary(models.Model):
    term = models.CharField(max_length=100)
    definition = models.TextField()
    picture = models.ImageField(null=True, blank="True", upload_to='glossary_pics')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.term

    class Meta:  
        db_table = "Glossary"