from django.shortcuts import render
import feedparser
from django.http import  HttpResponse

rss = feedparser.parse('https://www.ifpb.edu.br/ifpb/pedrasdefogo/noticias/todas-as-noticias-do-campus-pedras-de-fogo/RSS')

#nesse código ainda falta o parâmetro 'published' para automatizar o processo de RSS.

def iterate_entries(start_index, end_index):
    entries = rss.entries[start_index:end_index]
    data_list = []
    for entry in entries:
        data = {
            'url_noticia': entry['link'],
            'titulo_noticia': entry['title'],
            'img_href': None,
            'img_alt': entry['title'].upper(),
            'noticia_descricao': entry['summary']
        }
        data_list.append(data)
    return data_list

start_index = 0  # Posição de início
end_index = 3  # Posição de fim (não inclusiva)
data = iterate_entries(start_index, end_index)

def dados_email_view(request):
    dados_list = [
        
    ]
    dados_list.extend(data)  # Adiciona os dados obtidos da função iterate_entries
    return render(request, 'polls/email.html', {'dados': dados_list})


    