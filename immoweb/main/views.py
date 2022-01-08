from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def root(request):
    return render(request,'main/home.html')






def test00(request):
    print('main page is ok')
    return render(request,'main/for_test.html' )


def test01(request):
    print('this is test01')
    #return HttpResponse('plop')
    return render(request,'main/test.html' )


# Create your views here.
