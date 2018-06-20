a=10
b=5
print(a)
print(b)
a,b=b,a
print(a)
print(b)

lista1=[]

while(True):
    item=int(input("Digite um item para a lista (numero inteiro): "))
    if item<0:
        break
    lista1.append(item)

itens=len(lista1)
for contador2 in lista1:
    for contador in range(0,itens-1):
        if lista1[contador]>lista1[contador+1]:
            lista1[contador],lista1[contador+1]=lista1[contador+1],lista1[contador]
print(lista1)