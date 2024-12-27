def executar_caso(caso):
    if caso == 1:
        return "Executando caso 1"
    elif caso == 2:
        return "Executando caso 2"
    elif caso == 3:
        return "Executando caso 3"
    else:
        return "Executando caso padrão"


caso = int(input('Escolha o caso 1, 2 ou 3: '))

print(executar_caso(caso))
