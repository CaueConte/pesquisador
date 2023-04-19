from GoogleNews import GoogleNews

while True:
    print('Siglas mais comuns: en(inglês), pt(português), ru(russo), fr(francês), de(alemão)')
    idioma = input('Digite a sigla do idioma: ')

    if len(idioma) <= 2 and ' ' not in idioma:
        break
    else:
        print('sigla invalida')

palavra_chave = input('Digite a pesquisa: ')
print('Pesquisando, aguarde \n')

googlenews = GoogleNews(period = '8d')
googlenews.setlang(idioma)
googlenews.setencode('utf-8')
googlenews.search(palavra_chave)
noticias_link = googlenews.get_links()

titulo_noticia = googlenews.get_texts()

if idioma == 'en':
    print('News: \n')
elif idioma == 'pt':
    print('noticias: \n')
elif idioma == 'ru':
    print('Новости: \n')
elif idioma == 'fr':
    print('Nouvelles: \n')
elif idioma == 'de':
    print('Nachricht: \n')

titulo_links = zip(titulo_noticia, noticias_link)
for titulo, link in titulo_links:

    print(titulo+ ':')
    print(link)
    print('\n')

