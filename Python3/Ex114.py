'''
Ex 114 - Crie um codigo em Python que teste se o site Pudim está no computador usado.
'''
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://satsp.fazenda.sp.gov.br/COMSAT/Public/ConsultaPublica/ConsultaPublicaCfe.aspx')
except urllib.error.URLError:
    print('O site requisitado não está acessivel no momento')
else:
    print('Consegui acessar o site com sucesso!')
    print(site.read())
