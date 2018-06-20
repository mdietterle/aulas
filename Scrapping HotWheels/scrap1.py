import requests
from bs4 import BeautifulSoup

urlBase = "http://hotwheels.wikia.com/wiki/List_of_2017_Hot_Wheels"

pagina = requests.get(urlBase, timeout=5)

conteudoPagina = BeautifulSoup(pagina.content,"html.parser")

tabela = conteudoPagina.find_all(class_="wikitable")
link = tabela.find_all("a")
print(tabela)
print(link)