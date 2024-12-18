nome = input('Digite seu nome: ').lower()

#print(nome[::-1])

if nome == nome[::-1]:
    print('É um palindromo')
else:
    print('Não é um palindromo')