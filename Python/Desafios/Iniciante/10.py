nome = str(input())
salario = float(input())
totalVendas = float(input())

TOTAL = (totalVendas * 0.15) + salario

print(f"TOTAL = R$ {TOTAL:.2f}")