pessoas = int(input("Quantos amigos tem? "))
fatias = int(input("Quantas fatias tem? "))
comer = fatias // pessoas
resto = fatias % pessoas
print(f"cada pessoa vai comer" , comer,"fatias e vão sobrar" , resto, "fatias")

if fatias < pessoas:
    print("Quantidade de fatias menor que pessoas")
elif resto > 0:
  print("Sobrou ", resto, "prepare-se para a briga")