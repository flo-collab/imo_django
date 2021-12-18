from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from upload_csv.flo_functions import *
import os
import io


def upload(request):
    return render(request,'upload_csv/upload.html')

def post_csv(request):
    if request.method == 'POST' and 'myfile' in request.FILES:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        path = settings.MEDIA_ROOT+'\\'+os.listdir(settings.MEDIA_ROOT)[0]
        df_to_db(path)
        print("nb d'objet:",Bien.objects.count())
        return render(request,'upload_csv/green.html')


    elif (request.method == 'POST' and ('myfile' not in request.FILES)): 
        return render(request,'upload_csv/red.html')


    else:
        return render(request,'upload_csv/oups.html')






def upload_succes(request):
    context = {'val' :  "vayvoir si c'est transmi"}
    return render(request,'upload_csv/page_succes.html',context)

def test(request):
    return render(request,'upload_csv/test.html')

def test_v2(request):
    return render(request,'upload_csv/test_harder.html')


        # in_mem_to_db(myfile)
        # print('doss courant',os.getcwd())
        # file = myfile.read().decode('utf-8')
        # reader = csv.reader(io.StringIO(file))
        # next(reader)
        # null_counter = 0
        # for r in reader:
        #     for i in range(len(r)):
        #         if r[i] =='':
        #             null_counter +=1
        #             r[i]= None

        #     bien = Bien()
        #     bien = val_to_field(bien,r)
        #     bien.save()




        # in_mem_to_db(myfile)
        # print('doss courant',os.getcwd())
        # file = myfile.read().decode('utf-8')
        # reader = csv.reader(io.StringIO(file))
        # next(reader)
        # list_test = []
        # for r in reader:
        #    list_test.append(r)
        # print(list_test[0])





        # in_mem_to_db(myfile)
        # print('doss courant',os.getcwd())
        # file = myfile.read().decode('utf-8')
        # reader = csv.reader(io.StringIO(file))
        # next(reader)
        # null_counter = 0
        # for r in reader:
        #     for i in range(len(r)):
        #         if r[i] =='':
        #             null_counter +=1
        #             r[i]= None

        #     bien = Bien()
        #     bien = val_to_field(bien,r)
        #     bien.save()
        # print("nb d'objet:",Bien.objects.count())