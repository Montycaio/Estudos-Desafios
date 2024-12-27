salario = 1

while salario != 0:
    
    salario = int(input('Digite o salário do funcionário: '))

    if salario <= 500:
        bonus = salario + (salario * 0.10)
        print(f'O Salário final será {bonus}')
    else:
        print(f'O Salário final será {salario}')
        