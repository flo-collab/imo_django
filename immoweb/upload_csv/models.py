from django.db import models



class Bien(models.Model):
    id = models.fields.IntegerField(primary_key=True)
    id_lot = models.fields.CharField(max_length=100)
    nb_piece = models.fields.FloatField(blank=True,null=True)
    typologie = models.fields.CharField(max_length=100)
    prix_tva_reduite = models.fields.FloatField(blank=True,null=True)
    prix_tva_normale = models.fields.FloatField(blank=True,null=True)
    prix_HT = models.fields.FloatField(blank=True,null=True)
    prix_m2_HT = models.fields.FloatField(blank=True,null=True)
    prix_m2_TTC = models.fields.FloatField(blank=True,null=True)
    surface = models.fields.IntegerField(blank=True)
    etage = models.fields.CharField(max_length=10,blank=True,null=True)
    orientation = models.fields.CharField(max_length=100)
    exterieur = models.fields.BooleanField(default=False)
    balcony = models.fields.BooleanField(default=False)
    garden = models.fields.BooleanField(default=False)
    parking = models.fields.IntegerField(default=0)
    nom_programme = models.fields.CharField(max_length=100,blank=True)
    ville = models.fields.CharField(max_length=100)
    departement = models.fields.CharField(max_length=100)
    date_fin_programme = models.fields.CharField(max_length=100)
    adresse_entiere = models.fields.CharField(max_length=100)
    promoteur = models.fields.CharField(max_length=100,blank=True)
    date_extraction = models.fields.CharField(max_length=100)