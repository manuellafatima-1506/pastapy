compra=float(input("Qual o valor da sua compra? "))
desconto= (compra * 0.15)
final = (compra - desconto)
if compra > 100:
    print(f"R${final:.2f} você obteve desconto de R${desconto:.2f}")
else:
    print(f"Sua compra ficou R${compra}")
