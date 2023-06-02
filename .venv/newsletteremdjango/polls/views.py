from django.shortcuts import render

# Create your views here.

from django.http import  HttpResponse

def dadosemailview(request):
    dados_list = [
        {'urlnoticia': 'https://facebook.com', 'noticiatitulo': 'olha a pedra', 'urlimg': 'https://raw.githubusercontent.com/MatheusHFerreiraLima/HTML-CSS/main/imagens/AUTO-F1-ITA-FERRARI-SF-23.webp' , 'imgdescricao': 'descriçao imagem teste', 'noticiadescricao': 'AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH!'}, 

        {'urlnoticia': 'https://facebook.com', 'noticiatitulo': 'olha a pedra', 'urlimg': 'https://raw.githubusercontent.com/MatheusHFerreiraLima/HTML-CSS/main/imagens/AUTO-F1-ITA-FERRARI-SF-23.webp' , 'imgdescricao': 'descriçao imagem teste', 'noticiadescricao': 'HAHHAHAHHHHHHHHHHHHHHHHHH'},

        {'urlnoticia': None, 'noticiatitulo': None, 'urlimg': None , 'imgdescricao': None, 'noticiadescricao': None},
        ]
    return render(request, 'polls/email.html', {'dados': dados_list})


    