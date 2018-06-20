import time

now = time.localtime()
print(now[3],":",now[4],now[5])
agora=time.asctime(time.localtime(time.time()))
print(agora)
print(agora[11:19])
arquivo = open("teste.txt" ,"w+")
hora = agora[11:19]
arquivo.write(hora)
