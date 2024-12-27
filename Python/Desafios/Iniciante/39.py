
def calculadora():
    while True:

        n1 = input('Calculadora (exemplo: 1 + 2): ')

        entrada = n1.split()

        print(n1)
        print(entrada)

        num1 = float(entrada[0])
        num2 = float(entrada[2])
        op = entrada[1]

        try:
            if op == '+':
                resultado = num1 + num2
                print(resultado)
            elif op == '-':
                resultado = num1 - num2
                print(resultado)
            elif op == '*':
                resultado = num1 * num2
                print(resultado)
            elif op == '/':
                resultado = num1 / num2
                print(resultado)
            else:
                return print('Operador não identificado')
            
        except ZeroDivisionError:
            print('Erro ao dividir por 0')
        except Exception as e:
            print(f'Insira espaço entre cada numero e operador {e}')

calculadora()