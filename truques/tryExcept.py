dicionario = {'Maria': '1235'}

try:
    valor = dicionario['chave'] 
except KeyError:
    valor = None
print(valor)