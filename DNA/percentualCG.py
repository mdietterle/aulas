
def lerDNA():
    nome = input("Digite o nome do arquivo: ")
    arquivo = open("./DNA/"+nome,"r")
    dna=arquivo.readline()
    return dna

def calculapercentualCG(dna):
    contaC=dna.count("C")
    contaG=dna.count("G")
    totalCG=contaC+contaG
    tamanho=len(dna)
    percentual= (totalCG/tamanho)*100
    print(percentual)
    
dna=lerDNA()
#print(dna)
calculapercentualCG(dna)
