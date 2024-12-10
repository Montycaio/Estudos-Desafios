palavra = input("Digitie uma palavra: ").lower()

if palavra == palavra[::-1]:
    print("É um palindromo")
else:
    print("Não é um palindromo")
