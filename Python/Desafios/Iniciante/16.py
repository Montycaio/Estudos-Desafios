def converter_tempo(segundos):
    horas = segundos // 3600
    segundos_restantes = segundos % 3600
    minutos = segundos_restantes // 60
    segundos_finais = segundos_restantes % 60
    return f"{horas}:{minutos}:{segundos_finais}"

# Leitura do valor de entrada
N = int(input("Digite o tempo de duração em segundos: "))

# Conversão e exibição do resultado
resultado = converter_tempo(N)
print(resultado)
