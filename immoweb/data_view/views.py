from django.shortcuts import render
from django.conf import settings
from upload_csv.models import Bien
from data_view.models import Ville
from data_view.models import Send_mail
from django.core.mail import send_mail

import os
import pandas as pd
import numpy as np

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

    json_ville = df_ville.to_json(orient="values")
    return Ville.objects.all(), json_ville

def avg_price_and_count(path):
    df = pd.read_csv(path)
    df = df[df['balcony']==False]
    mean_price = round(df['prix_tva_normale'].mean(),1)
    nb_bien = len(df)
    return mean_price, nb_bien


def visualize(request):
    print('page visualize')
    biens = Bien.objects.all()
    path = settings.MEDIA_ROOT+'\\'+os.listdir(settings.MEDIA_ROOT)[0]
    villes, json_ville = ville_to_db(path)
    mean_price, nb_bien = avg_price_and_count(path)
    data_json = {'data_villes':json_ville,'nb_biens':nb_bien,'mean_price':mean_price}

    context = {'biens':biens, 'villes':villes, 'mean_price':mean_price}
    return render(request,'data_view/visualize_data.html',context)




def visualize_send_mail(request):
    biens = Bien.objects.all()
    path = settings.MEDIA_ROOT+'\\'+os.listdir(settings.MEDIA_ROOT)[0]
    villes = ville_to_db(path)
    mean_price, nb_bien = avg_price_and_count(path)
    context = {'biens':biens, 'villes':villes, 'mean_price':mean_price}
    message = (Send_mail.objects.all()[0].message
    .replace('{mean_price}',str(mean_price))
    .replace('{nb_bien}',str(nb_bien)))
    send_mail(Send_mail.objects.all()[0].sujet,
                message,
                settings.EMAIL_HOST_USER,
                [Send_mail.objects.all()[0].mail_destinataire])

    return render(request,'data_view/visualize_data.html',context)
