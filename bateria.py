bateria = int(input("Qual a porcentagem do seu telefone? "))
tempo = int(input("Quantos porcento ele consome por hora? "))
resposta = bateria // tempo
if bateria <= 20:
    print("corre pra tomada, ainda te resta: ",resposta, "horas" )
else:
    print("Ainda te resta", resposta, "horas" )