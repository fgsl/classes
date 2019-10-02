# coding: utf-8
import requests # não disponível por padrão, instalar com pip install requests
from lxml.html import fromstring
import json 

page = requests.get("https://www.isulpar.edu.br/institucional/dirigentes.html")
elements =   fromstring(page.text).cssselect("p > strong")

dirigentes = []

for element in elements:
    dirigentes.append(element.text or u'')
f = open("dirigentes.json", "w")
json.dump(dirigentes, f)
