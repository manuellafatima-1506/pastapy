velo_max= float(input("Qual a velocidade máxima da via?"))
velocidade=float(input("Qual a velocidade registrada pelo radar?"))
conta= velocidade - velo_max
if velocidade> velo_max:
    print(f"você exedeu o limite por {conta}km/h e recebeu uma multa de 130,16" )
else:
    print("Boa viagem!")
