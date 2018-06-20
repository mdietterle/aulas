dicionario={"um":1, "dois":20}

valor=dicionario.get("um")
print(valor)

#buscar um valor, e caso não exista, vai retornar o valor final
print(dicionario)
valor=dicionario.get("tres",3)
print(valor)
print(dicionario)
