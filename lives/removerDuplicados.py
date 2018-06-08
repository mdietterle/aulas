def criaLista():
    lista=[]
    while(True):
        item=input("Digite um item para a lista: ")
        if(item==""):
            break
        else:
            lista.append(item)
    return lista

def removeDuplicados(lista):
    listaLimpa=[]
    for item in lista:
        if item not in listaLimpa:
            listaLimpa.append(item)
    return listaLimpa

listaDuplos=criaLista()
print(listaDuplos)
listaFinal=removeDuplicados(lista2)
print(listaFinal)