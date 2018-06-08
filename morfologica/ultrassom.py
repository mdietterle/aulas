# pip intall <nome biblioteca>
from datetime import datetime
from dateutil.relativedelta import relativedelta
import xlrd
from datetime import date
from urllib.request import urlretrieve

print("Programa para calcular o prazo de exame de ultrassom")
print("que deverá ser feito entre 22 e 24 semanas de gestação")
print("Você deverá informar o número de semanas de gestação em que você se encontra")

semanas = int(input("Com quantas semanas de gestacão a paciente se encontra? "))
data_consulta = input("Emque data foi a consuta? ")

semanasInicio = 22 - semanas
semanaFinal = 24 -semanas 

d = datetime.strptime(data_consulta, "%d/%m/%Y").date()
morfologicoInicio = d + relativedelta(weeks=semanasInicio)
morfologicoFinal = d+relativedelta(weeks=semanaFinal)
dfinal = morfologicoFinal.strftime('%d/%m/%Y')
dinicial = morfologicoInicio.strftime('%d/%m/%Y')
print("O examen deve ser feito entre ",dinicial, "e ",dfinal)

dataExame = input("Em que dia deseja fazer o exame? ")
url=None
path=None

if not url:
    url='http://www.anbima.com.br/feriados/arqs/feriados_nacionais.xls'
if not path:
    path = 'feriados_nacionais.xls'
try:
    response=urlretrieve(url,filename=path)
    wb = xlrd.open_workbook(path)
except:
    
    print("Erro ao abrir o arquivo online, tentando versao offline...")
    wb = xlrd.open_workbook(path)
ws = wb.sheet_by_index(0)
i=1
dates=[]
diaSemana = []
descricao = []

while ws.cell_type(i,0)==3:
    y,m,d,_,_,_ = xlrd.xldate_as_tuple(ws.cell_value(i,0), wb.datemode)
    dates.append(date(y,m,d))
print(dates)

