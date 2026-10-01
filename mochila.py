peso=float(input("Qual o seu peso? "))
mochila=float(input("Qual o peso da mochila? "))
max= 0.10 * peso 
fim= (mochila/ peso) *100
if mochila >= max:
    print("Mochila pesada demais", fim, "%")
else:
    print("pode carregar", fim, "%")