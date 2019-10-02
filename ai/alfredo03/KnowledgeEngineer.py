# coding: utf-8
import config
import requests #não disponível por padrão, instalar com pip install requests
from lxml.html import fromstring
import json

class KnowledgeEngineer:
    def getFacts(self, question):
        page = requests.get("https://www.isulpar.edu.br/institucional/dirigentes.html")
        elements = fromstring(page.text).cssselect("p > strong")
        return []
