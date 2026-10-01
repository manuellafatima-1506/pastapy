distancia_drone = float (input("Qual a distancia percorrida pelo drone"))
tempo_gasto=float (input("Qual o tempo gasto em minutos: "))
hora = tempo_gasto / 60 
media = distancia_drone / hora
if media > 40:
    print(f"{media:.2f} modo turbo ativo!")
else:
    print(f"{media:2f} nada de turbo...")