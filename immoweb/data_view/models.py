from django.db import models

# Create your models here.
class Ville(models.Model):
    name = models.CharField(max_length=100,primary_key=True)
    avg_price = models.fields.FloatField()
    std_deviation = models.fields.FloatField(default=0,blank=True,null=True)