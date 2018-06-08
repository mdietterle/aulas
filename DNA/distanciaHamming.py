def lerDNA():
    nome = input("Digite o nome do arquivo: ")
    arquivo = open("./DNA/"+nome,"r")
    nome2= input("Digite o nome do arquivo: ")
    arquivo2 = open("./DNA/"+nome2,"r")
    dna=arquivo.readline()
    dna2=arquivo2.readline()
    return dna,dna2

def distanciaHamming(dna,dna2):
    diferenca=0
    for cont in range(1000):
        print(dna[cont],dna2[cont],end="")
        print("")
        if(dna[cont] != dna2[cont]):
            diferenca+=1
    print(diferenca)

dna,dna2=lerDNA()
distanciaHamming(dna,dna2)