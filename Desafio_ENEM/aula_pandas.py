import pandas as pd
import numpy as np

tamanho_bloco = 1e3
i=1
dados=0
#goo.gl/hqazog
file ="C:\\Users\\Martim\\OneDrive\\Scripts Python\\aulas\\Desafio_ENEM\\Enderecos_escolas_Jaragua_do_Sul.csv" 
colunas = ["Escola","Endereco","Numero","Bairro","Tipo"]
for pedaco in pd.read_csv(file,chunksize=tamanho_bloco,\
index_col=None,encoding="latin-1",usecols=colunas,\
delimiter=","):
    pedaco=pedaco.dropna(subset=colunas)
    pedaco["nota"]="Test"
    #print(pedaco)
    pedaco=pedaco.sort_values("Numero",ascending=True)
    print(pedaco.head(20))
    print("Foram lidas %i linhas" %(tamanho_bloco))





