import pandas as pd
import time
import psutil
import numpy as np
import multiprocessing as mp

num_cores = mp.cpu_count()
print("Este processador tem ",num_cores,"nucleos. Uso da memória:",psutil.virtual_memory())

tamanho_bloco = 1e6 #1 milhão
start_time = time.time()
i=1
check=0
file="C:\\Users\\Martim\\Downloads\\Compressed\\microdados_enem2016\\microdados_enem_2016.csv"
indice=['NU_INSCRICAO']
colunas=['NU_INSCRICAO','TP_PRESENCA_CN','TP_PRESENCA_CH','TP_PRESENCA_LC','TP_PRESENCA_MT','NU_NOTA_CN','NU_NOTA_CH','NU_NOTA_LC','NU_NOTA_MT','TP_STATUS_REDACAO','NU_NOTA_REDACAO']
print("Iniciando leitura e filtragem dos dados... ")
print("Cada loop lê 1 milhão de linhas do arquivo...")
print("------------------------------------------------------------------------------")
for chunk in pd.read_csv(file,chunksize=tamanho_bloco,index_col=None,encoding="latin-1",usecols=colunas,delimiter=";"):
	chunk=chunk.dropna(subset=colunas)
	if(i==1):
		chunk[chunk.TP_PRESENCA_CN == 1]
		chunk[chunk.TP_PRESENCA_CH == 1]
		chunk[chunk.TP_PRESENCA_LC == 1]
		chunk[chunk.TP_PRESENCA_MT == 1]
		chunk[chunk.TP_STATUS_REDACAO == 1]
		result = chunk
		print("Numero de linhas  úteis, já descartadas provas eliminadas: ",chunk.shape[0])#result.shape[0])
		print("Loop ",i,"demorou %s segundos..." % (time.time() - start_time))
		i+=1
		chunk['teste']=((chunk.NU_NOTA_CN*2)+chunk.NU_NOTA_CH+(chunk.NU_NOTA_MT*3)+(chunk.NU_NOTA_LC*1.5)+(chunk.NU_NOTA_REDACAO*3))/5
		check=check+chunk.shape[0]
	else:
		chunk[chunk.TP_PRESENCA_CN == 1]
		chunk[chunk.TP_PRESENCA_CH == 1]
		chunk[chunk.TP_PRESENCA_LC == 1]
		chunk[chunk.TP_PRESENCA_MT == 1]
		chunk[chunk.TP_STATUS_REDACAO == 1]
		result=result.append(chunk)
		print("Numero de linhas  úteis, já descartadas provas eliminadas: ",chunk.shape[0])#result.shape[0])
		print("Loop ",i,"demorou %s segundos..." % (time.time() - start_time))
		i+=1
		chunk['teste']=((chunk.NU_NOTA_CN*2)+chunk.NU_NOTA_CH+(chunk.NU_NOTA_MT*3)+(chunk.NU_NOTA_LC*1.5)+(chunk.NU_NOTA_REDACAO*3))/5
		check=check+chunk.shape[0]
		
	del(chunk)    
print("Carregamento terminado... mostrando informações...")
print(result.shape)
print("-" * 100)
print("Mostrando 20 primeiros resultados do dataframe...")

print(result.head(20))
print("------------------------------------------------------------------------------")
print("Ordenando resultados...")
final=result.sort_values("teste", ascending=False)
print("Mostrando os 20 melhor classificados no EMEM 2016, com todas as notas inclusas")
print(final.head(20))
print("------------------------------------------------------------------------------")
print("Mostrando somente campos de interesse...")
print(final[['NU_INSCRICAO','teste']].head(20))
print("Fim do processamento...")