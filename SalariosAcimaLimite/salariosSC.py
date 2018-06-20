# salario ministro stf R$ 33.763 
limite = 33763*0.9
import csv
contador=0
listasalarios = open("C:\\Users\\Martim\\Documents\\salariosSC.csv",'r',encoding="UTF-8")
lista = csv.reader(listasalarios,delimiter=";")
#lista = listasalarios.readlines() # readlinesssssss
#listasalarios.close()
for servidor in lista:
    #print(servidor)
    if(servidor[0]=="Nome"):
        continue
    if (float(servidor[2])>=limite):
        print(servidor[0], "recebe salário de R$", servidor[2], "e trabalha como ", servidor[3] )
        print("-----------------------------------------------------------------------------------------------")
        contador+=1
listasalarios.close()
print("Total de salários acima do teto permitido: ", contador)