#função para criar lista até que seja deixado em branco
def criaLista():
    lista=[]
    while(True):
        #fazer a leitura do item
        item=input("Digite um item para a lista: ")
        #testa se o item é branco, se for para o loop while, senão adiciona o item na lista
        if(item ==""):
            break
        else:
            #lista.append(item) vai adicionar o item ao final da lista
            lista.append(item)
    return lista

def removeDuplos(lista):
    listaLimpa=[]
    for item in lista:
        if item not in listaLimpa:
            listaLimpa.append(item)
    return listaLimpa


listaDuplos=criaLista()
print(listaDuplos)
listaFinal=removeDuplos(listaDuplos)
print(listaFinal)