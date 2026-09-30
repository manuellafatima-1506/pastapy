salgado = float(input("Qual o preço do salgado? "))
dinheiro = float (input("Quanto você tem? "))
troco = dinheiro - salgado
if dinheiro < salgado:
    print ("Saldo insuficiente, faminto!")
else:
    print ("seu troco é de:", troco, "reais")