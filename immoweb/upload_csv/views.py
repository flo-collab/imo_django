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



