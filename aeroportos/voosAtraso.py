# mostrar voos que sairam atrasados do local de origem


import csv
voo = open('C:\\Users\\Martim\\OneDrive\\Scripts Python\\aeroportos\\vra.csv', 'r')
justificativa = open('C:\\Users\\Martim\\OneDrive\\Scripts Python\\aeroportos\\justificativas.csv', 'r')
justificativas = csv.reader(justificativa, delimiter=";", quoting=csv.QUOTE_NONE)
voos = csv.reader(voo, delimiter=';', quoting=csv.QUOTE_NONE)
'''
for linha in voos:
    if linha[11]=="Código Justificativa":
        continue
    print("linha ", linha[11])
    for just in justificativas:
        print("justificativa ",just[0])
        if just[0]=="Sigla Justificativa":
            continue
        if(linha[6]<linha[7]): # and (just[0].lower()==linha[11].lower()):
            #print("justifi", just[0])
            #print("Linha", linha[11])
            if (just[0]==linha[11]):
                print("o voo ",linha[3], "atrasou por ", just[1])
#        break
#    break
'''

for linha in voos:
    for just in justificativas:
        if (linha[6] < linha[7]):
            print(linha[11])
            print(just[1])
            if (just[0]==linha[11]):
                print("finalmente")