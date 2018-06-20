

ref_arquivo = open("C:\\Users\\Martim\\Documents\\qbs.txt","r")
for linha in ref_arquivo:
    valores = linha.split()
    print(valores[4], valores[0], valores[1], valores[2], 'lançou ', valores[10], 'jardas por jogo.' )

ref_arquivo.close()