import feedparser

rss = feedparser.parse('https://www.ifpb.edu.br/ifpb/pedrasdefogo/noticias/todas-as-noticias-do-campus-pedras-de-fogo/RSS')


def iterate_entries(start_index, end_index):
    entries = rss.entries[start_index:end_index]
    for entry in entries:
        print(entry['title'])
        print(entry['link'])
        print(entry['summary'])
        print(entry['published'])
        print('---')


start_index = 0  # Posição de início
end_index = 3  # Posição de fim (não inclusiva)
iterate_entries(start_index, end_index)
