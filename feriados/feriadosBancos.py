import xlrd
from datetime import date
from urllib.request import urlretrieve

def holidays(url=None, path=None):
    if not url:
        url = 'http://www.anbima.com.br/feriados/arqs/feriados_nacionais.xls'
    if not path:
        path = 'feriados_nacionais.xls'
    try:
        wb = xlrd.open_workbook(path)
    except:
        response = urlretrieve(url, filename=path)
        wb = xlrd.open_workbook(path)
    ws = wb.sheet_by_index(0)
    i = 1
    dates = []
    dias=[]
    desc=[]
    while ws.cell_type(i, 0) == 3:
        y, m, d, _, _, _ = xlrd.xldate_as_tuple(ws.cell_value(i, 0), wb.datemode)
        dates.append(date(y, m, d))
        i += 1
        dias.append(ws.cell_value(i,1))
        desc.append(ws.cell_value(i,2))
    return dates,dias,desc


if __name__ == '__main__':
    datas,diasSemana,descricao = holidays()
    print(datas)
    print(diasSemana)
    print(descricao)