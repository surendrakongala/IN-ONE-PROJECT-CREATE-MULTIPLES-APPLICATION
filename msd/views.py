from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def msd(request):
    return render(request,'msd.html')
def macha(request):
    return  HttpResponse('<h1><center>BEST PLAYER</center></h1>')
