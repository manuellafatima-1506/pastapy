nota1 =float(input("diga a nota? "))
nota2 =float(input("diga a nota? "))
nota3 =float(input("diga a nota? "))
media = (nota1+ nota2+ nota3) /3
if media >= 6.0:
    print(f"Aprovado, {media:.2f}")
else:
    print(f"Recuperação, {media:.2f}")