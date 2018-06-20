import os
global arquivo
def abrecriar():
    global arquivo
    arquivo = open("nome.txt", "w+")

def abreappend():
    global arquivo
    arquivo = open("nome.txt", "a+")

def qualquer():
    global arquivo
    #se arquivo existe, somente abre
    if(os.path.isfile("nome.txt")):
        abreappend()
    else:
        abrecriar()
    arquivo.write("teste")

qualquer()