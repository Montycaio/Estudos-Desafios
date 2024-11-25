# Lendo os dados da primeira peça
codigo1, quantidade1, valor_unitario1 = input().split()
codigo1 = int(codigo1)
quantidade1 = int(quantidade1)
valor_unitario1 = float(valor_unitario1)

# Lendo os dados da segunda peça
codigo2, quantidade2, valor_unitario2 = input().split()
codigo2 = int(codigo2)
quantidade2 = int(quantidade2)
valor_unitario2 = float(valor_unitario2)

# Calculando o valor total a pagar
valor_a_pagar = (quantidade1 * valor_unitario1) + (quantidade2 * valor_unitario2)

# Exibindo o resultado formatado com 2 casas decimais
print(f"VALOR A PAGAR: R$ {valor_a_pagar:.2f}")