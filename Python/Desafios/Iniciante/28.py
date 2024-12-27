
def operacao():
        while True:
            n1 = int(input('Digite um número: '))
            n2 = int(input('Digite um número: '))

            op = int(input('\nEscolha qual operacao irá utilizar:\n' + '1: Adição\n' + '2: Subtração\n' + '3: Divisão\n' + '4: Multiplicação\n' + '5: Sair\n' + 'Digite a opção aqui: \n\n'))
            #retorno = 1
            if op == 1:
                res = n1 + n2
                print(f'Resultado: {res}')
            elif op == 2:
                res = n1 - n2
                print(f'Resultado: {res}')
            elif op == 3:
                res = n1 / n2
                print(f'Resultado: {res}')
            elif op == 4:
                res = n1 * n2
                print(f'Resultado: {res}')
            elif op == 5:
                print('Saindo...')
                break
            else:
                print('Opção inválida')

operacao()