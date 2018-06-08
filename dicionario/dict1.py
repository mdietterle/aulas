espanhol = {"um": "uno", "dois": "dos"}
ingles = {"um": "one", "dois": "two"}

idioma = input("Escolha o idioma: ")
if (idioma=="espanhol"):
    print(idioma+["um"])
elif (idioma=="ingles"):
    print(ingles["um"])
else:
    print("inválido")