nomes = input('Escreva varios nomes e separe por virgulas: ')

nomes = nomes.split(',')

nomes = [nome.replace('a', 'o') for nome in nomes]

print(nomes)