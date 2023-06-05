from django.shortcuts import render
import feedparser
from django.http import  HttpResponse
import time
import datetime
import django.core.mail import

# # rss = feedparser.parse('https://www.ifpb.edu.br/ifpb/pedrasdefogo/noticias/todas-as-noticias-do-campus-pedras-de-fogo/RSS')

# #nesse código ainda falta o parâmetro 'published' para automatizar o processo de RSS.

# # def iterate_entries(start_index, end_index):
# #     entries = rss.entries[start_index:end_index]
# #     data_list = []
# #     for entry in entries:
# #         data = {
# #             'url_noticia': entry['link'],
# #             'titulo_noticia': entry['title'],
# #             'img_href': None,
# #             'img_alt': entry['title'].upper(),
# #             'noticia_descricao': entry['summary']
# #         }
# #         data_list.append(data)
# #     return data_list

# # start_index = 0  # Posição de início
# # end_index = 3  # Posição de fim (não inclusiva)
# # data = iterate_entries(start_index, end_index)

# # def dados_email_view(request):
# #     dados_list = [
        
# #     ]
# #     dados_list.extend(data)  # Adiciona os dados obtidos da função iterate_entries
# #     return render(request, 'polls/email.html', {'dados': dados_list})




# feed_url = 'https://www.ifpb.edu.br/ifpb/pedrasdefogo/noticias/todas-as-noticias-do-campus-pedras-de-fogo/RSS'

# def get_initial_time():
#     return time.time()

# # def iterate_entries():
#     # rss = feedparser.parse(feed_url)
#     # entries = rss.entries
#     # data_list = []
#     # initial_time = get_initial_time()
#     # for entry in entries:
#     #     published_time = time.mktime(entry.published_parsed)
#     #     if published_time > initial_time:
#     #         data = {
#     #             'url_noticia': entry.link,
#     #             'titulo_noticia': entry.title,
#     #             'img_href': None,
#     #             'img_alt': entry.title.upper(),
#     #             'noticia_descricao': entry.summary
#     #         }
#     #         data_list.append(data)
#     # return data_list


# print(get_initial_time())
# # Exemplo de uso:
# # data = iterate_entries()

# def dados_email_view(request):
#     dados_list = []
#     dados_list.extend(data)  # Adiciona os dados obtidos da função iterate_entries
#     return render(request, 'polls/email.html', {'dados': dados_list})

######### DADOS DE TESTE QUASE DEFINITIVO:

a=0
# feed_url = 'https://www.ifpb.edu.br/ifpb/pedrasdefogo/noticias/todas-as-noticias-do-campus-pedras-de-fogo/RSS'

# def get_initial_time():
#     return time.time()

# initial_time = get_initial_time()

# def iterate_entries():
#     rss = feedparser.parse(feed_url)
#     entries = rss.entries
#     data_list = []
#     for entry in entries:
#         published_time = time.mktime(entry.published_parsed)
#         if published_time > initial_time:
#             data = {
#                 'url_noticia': entry['link'],
#                 'titulo_noticia': entry['title'],
#                 'img_href': None,
#                 'img_alt': entry['title'].upper(),
#                 'noticia_descricao': entry['summary']
#             }
#             data_list.append(data)
#     return data_list

# dados_chamada= iterate_entries()

# def dados_email_view(request):
#     dados_list = [

#     ]
#     dados_list.extend(dados_chamada)  # Adiciona os dados obtidos da função iterate_entries
#     return render(request, 'polls/email.html', {'dados': dados_list})




# # Loop infinito
# while True:
# # Obter a data e hora atual
#     current_datetime = datetime.datetime.now()

# # Verificar se o dia atual é uma quinta-feira
#     if current_datetime.weekday() == 3:  # 3 representa quinta-feira (segunda-feira é 0)
#     # Puxando novas chamadas, que consequentemente puxam novos dados da outra função
#         atualizacao = dados_email_view(request)

#         #estou pensando em colocar um:
#         #if iterate_entries() == []:
#             #não mande e-mail
#         #else:
#             #mandar email

#     # Processar os dados obtidos, por exemplo, enviá-los por e-mail, salvar em um arquivo, etc.
#     # Aqui você pode adicionar a lógica necessária para lidar com os dados
    
#     # Atualizar o tempo inicial para evitar repetição de entradas já processadas
#         initial_time = time.time()

# # Aguardar até a próxima quinta-feira
# # Calcular o tempo restante até a próxima quinta-feira
#     next_thursday = current_datetime + datetime.timedelta((3 - current_datetime.weekday() + 7) % 7)
#     time_delta = next_thursday - current_datetime

# # Aguardar o tempo restante até a próxima quinta-feira
#     time.sleep(time_delta.total_seconds())
a=0


def envia_email_view(request):
    return HttpResponse("tetsando") 