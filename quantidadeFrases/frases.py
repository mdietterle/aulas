arquivo=open("C:\\Users\\Martim\\OneDrive\\Scripts Python\\aulas\\quantidadeFrases\\rush.txt","r")
pontos=exclamacoes=interrogacoes=reticencias=0
while(True):
	texto=arquivo.readline()
	if texto=='':
		break
	pontos=pontos+ texto.count(".")
	exclamacoes=exclamacoes+texto.count("!")
	interrogacoes=interrogacoes+texto.count("?")
	reticencias=reticencias+texto.count("...")
	print(texto)
	desconto=reticencias*3
print(pontos-desconto)