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
    complementar=""
    for acido in dna:
        if acido=="A":
            baseComplementar="T"
        elif acido=="T":
            baseComplementar="A"
        elif acido=="C":
            baseComplementar="G"
        else:
            baseComplementar="C"
        complementar = complementar+baseComplementar
    return complementar[::-1]

def gravaComplementar(comp,nome):
    arquivo = open("./DNA/Comple2"+nome,"w")
    arquivo.write(comp)
    arquivo.close()

dna,nome=lerDNA()
comp=dnaComplementar2(dna)
print(comp)
gravaComplementar(comp,nome)