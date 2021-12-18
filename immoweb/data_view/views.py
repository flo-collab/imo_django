from django.shortcuts import render
from django.conf import settings
from upload_csv.models import Bien
from data_view.models import Ville
import os
import pandas as pd
# Create your views here.

def ville_to_db(path):
    df = pd.read_csv(path)
    df = df[df['balcony']==False]
    df_ville = round(df.groupby('ville')['prix_tva_normale'].agg(['mean','std']).reset_index(),1).fillna(0)
    df_list = df_ville.values.tolist()
    for row in df_list:
        ville = Ville()
        ville.name= row[0]
        ville.avg_price = row[1]
        ville.std_deviation= row[2]
        ville.save()
    print(Ville.objects.count())
    return Ville.objects.all()



def visualize(request):
    print('page visualize')
    biens = Bien.objects.all()
    path = settings.MEDIA_ROOT+'\\'+os.listdir(settings.MEDIA_ROOT)[0]
    villes = ville_to_db(path)
    context = {'biens':biens, 'villes':villes }
    return render(request,'data_view/visualize_data.html',context)