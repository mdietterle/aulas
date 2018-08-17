#URL http://www.buscape.com.br/pesquise-uma-loja.html?pg=1
#from 1 to 21265
# $('.size1of3').each(function() {var x = $(this).find('a:first');console.log(x.attr('title') + ' ' + x.attr('href'))});
import requests
import bs4
import openpyxl
import logging
from openpyxl import Workbook
#iniciar o arquivo de log
logging.basicConfig(filename='arq_links.log',level=logging.WARNING)
#iniciar a planilha do excel otimizada para escrita
wb = Workbook(write_only = True)
ws = wb.create_sheet()
for i in range(1,194): 
  #try:
  payload = {'joinville-sc?page=':str(i)}
  response = requests.get('https://cep.guiamais.com.br/busca', params = payload)
  print(response.text)
  soup = bs4.BeautifulSoup(response.text)
  #print(soup)
  for tabela in soup.find_all(class_='table s_table_box table-striped table-responsive'):
    #print(tabela)
    ws.append(tabela)

     #print "#%s" % i,
  #except Exception as err:
   #print "Erro na pagina %s" % i
   #logging.exception(u"Erro na pagina %s" % i) 
wb.save('lojas.xlsx')