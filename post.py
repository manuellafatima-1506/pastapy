texto=(input("Digite seu texto: "))
quantidade = len(texto)
if quantidade > 280:
    print("Exedeu o limite de caracteres", quantidade)
else:
    print("menor", quantidade)