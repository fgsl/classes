# coding: utf-8
import requests # não disponível por padrão, instalar com pip install requests
from lxml.html import fromstring
import json 

page = requests.get("https://www.isulpar.edu.br/institucional/missao.html")
elements =   fromstring(page.text).cssselect("li > span > a")

for element in elements:
    print element.get('href')