from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def upload(request):
    return render(request,'upload_csv/upload.html')

def upload_succes(request):
    context = {'val' :  "vayvoir si c'est transmi"}
    return render(request,'upload_csv/page_succes.html',context)



def test(request):
    return render(request,'upload_csv/test.html')

def test_v2(request):
    return render(request,'upload_csv/test_harder.html')