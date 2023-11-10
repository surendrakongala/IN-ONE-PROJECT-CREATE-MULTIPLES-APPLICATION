from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def kohali(request):
    return render(request,'virat.html')
def macha1(request):
    return HttpResponse('<h1><center>BEST BATSMAN</center></h1>')
