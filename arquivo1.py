import feedparser

rss = feedparser.parse('https://www.ifpb.edu.br/ifpb/pedrasdefogo/noticias/todas-as-noticias-do-campus-pedras-de-fogo/RSS')

print(rss)


