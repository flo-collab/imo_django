from upload_csv.models import Bien
import csv
import io
import pandas as pd
import numpy as np

def df_to_db(path):
    df = pd.read_csv(path)
    df = df[df['balcony']==False]
    df_list = df.values.tolist()
    for r in df_list:
        for i in range(len(r)):
            if r[i] ==np.nan:
                r[i]= None
        bien = Bien()
        bien = val_to_field(bien,r)
        bien.save()
        print("nb d'objet:",Bien.objects.count())



def in_mem_to_db(myfile):
    for r in in_mem_to_reader(myfile):
        bien = Bien()
        bien = val_to_field(bien,r)
        bien.save()
    print("nb d'objet:",Bien.objects.count())
    return Bien
    
def in_mem_to_reader(myfile):
    file = myfile.read().decode('utf-8')
    reader = csv.reader(io.StringIO(file))
    next(reader)
    null_counter = 0
    for r in reader:
        for i in range(len(r)):
            if r[i] =='':
                null_counter +=1
                r[i]= None
    print('nb de null = ', null_counter )
    return reader


def val_to_field(bien,r):
    bien.id = r[0]
    bien.id_lot = r[1]
    bien.nb_piece = r[2]
    bien.typologie = r[3]
    bien.prix_tva_reduite = r[4]
    bien.prix_tva_normale = round(r[5],1)
    bien.prix_HT = r[6]
    bien.prix_m2_HT = r[7]
    bien.prix_m2_TTC = r[8]
    bien.surface = r[9]
    bien.etage = r[10]
    bien.orientation = r[11]
    bien.exterieur = r[12]
    bien.balcony = r[13]
    bien.garden = r[14]
    bien.parking = r[15]
    bien.nom_programme = r[16]
    bien.ville = r[17]
    bien.departement = int(r[18])
    bien.date_fin_programme = r[19]
    bien.adresse_entiere = r[20]
    bien.promoteur = r[21]
    bien.date_extraction = r[22]
    return bien


def csv_to_db(path):
    for r in path_csv_to_reader_v2(path):
        bien = Bien()
        bien = val_to_field(bien,r)
        bien.save()
        print("nb d'objet:",Bien.objects.count())
    return

def path_csv_to_reader(path):
    # version sqlite :
    f = open(rf'{path}', 'r')
    next(f)
    reader = csv.reader(f, delimiter = ',')
    for r in reader:
        for i in range(len(r)):
            if r[i] =='':
                r[i]= None

    print('lala')
    return reader

def path_csv_to_reader_v2(path):
# version sqlite :
    f = open(rf'{path}', 'r')
    next(f)
    reader = csv.reader(f, delimiter = ',')
    list_r =[]
    for r in reader:
        for i in range(len(r)):
            if r[i] =='':
                print('lala')
                r[i]= None
        list_r.append(r)
    return list_r
