from django.shortcuts import render

# Create your views here.

from django.http import  HttpResponse

def index(request):
    return HttpResponse("Olá, mundo! Eu estou lascado no meu TCC e o tempo está se encurtando.")
    #"Esta é a view mais simples possível no Django". Se eu não estou entendedo isso e nem python básico, imagina as mais complexas.