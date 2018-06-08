def lerDNA():
    nome = input("Digite o nome do arquivo: ")
    arquivo = open("./DNA/"+nome,"r")
    dna=arquivo.readline()
    return dna,nome

def dnaComplementar(dna):
    trans = str.maketrans('ATCG', 'TAGC')
    comp=dna.translate(trans)[::-1]
    print(dna)
    print(comp)
    return comp

def dnaComplementar2(dna):
    rna=""
    for acido in dna:
        if acido=="T":
            baseComplementar="U"
        else:
            baseComplementar=acido
        rna = rna+baseComplementar
    return rna

def gravaRNA(rna,nome):
    arquivo = open("./DNA/RNA"+nome,"w")
    arquivo.write(rna)
    arquivo.close()

dna,nome=lerDNA()
rna=dnaComplementar2(dna)
print(rna)
gravaRNA(rna,nome)