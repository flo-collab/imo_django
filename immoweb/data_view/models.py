from django.db import models

# Create your models here.
class Ville(models.Model):
    name = models.CharField(max_length=100,primary_key=True)
    avg_price = models.fields.FloatField()
    std_deviation = models.fields.FloatField(default=0,blank=True,null=True)

class Send_mail(models.Model):
    sujet = models.CharField(max_length=100, null = True)
    message = models.CharField(max_length=500, null = True)
    mail_destinataire= models.CharField(max_length=50, null = True)