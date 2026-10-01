horas=int(input("Quantas horas durou a impressão? "))
preco=float(input("Quanto vale o kwh? "))
conta= horas * 0.35
kw= conta*preco
print(f"Custo da impressão: R$ {kw:.2f} ")