lista=["pão","leite","queijo", "café","presunto"]

print(lista)

for compras in range(0,len(lista)):
    print(lista[compras])

item = input("Digite o item que você esqueceu de colocar na lista: ")

lista.append(item)

print(lista)
print("----------------------------")

for compras in lista:
    print(compras)
