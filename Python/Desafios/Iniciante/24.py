n1 = 1

while n1 != 0:

    n1 = int(input('Digite um numero: '))

    res = n1 % 5

    if res == 0:
        print('É divisivel por 5')
        
    else:
        print('Não é divisivel por 5')