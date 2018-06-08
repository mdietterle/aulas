import random
def geraDNA():
    dna=""
    for cont in range(10000):
        nucleotideo = random.randint(1,4)
        #print(nucleotideo)
        if (nucleotideo==1):
            acido="A"
        elif (nucleotideo==2):
            acido="C"
        elif (nucleotideo==3):
            acido="T"
        else:
            acido="G"
        dna = dna+acido
    print(dna)
    return dna

def gravaDNA(dna):
    nome = input("Digite o nome do arquivo: ")
    arquivo = open("./DNA/alunos/"+nome,"w")
    arquivo.write(dna)
    arquivo.close()


dna = geraDNA()
gravaDNA(dna)