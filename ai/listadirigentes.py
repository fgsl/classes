# coding: utf-8
import json 

f = open("dirigentes.json", "r")
dirigentes = json.load(f)

for dirigente in dirigentes:
    print dirigente

