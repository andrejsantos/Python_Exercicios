# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
import urllib
import urllib.request
try:
    site = urllib.request.urlopen('https://www.google.com.br/?gws_rd=cr&ei=7yt5UsfTK-bIsAThooDABg')
except:
    print('ERRO!')
else:
    print('DEU BOM!')