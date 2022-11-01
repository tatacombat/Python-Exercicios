import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site está indisponível.')
else:
    print('Consegui acessar o site Pudim com Sucesso!')
 #   print(site.read())# ler o conteúdo html do site