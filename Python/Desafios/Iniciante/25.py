n1 = int(input('Digite número n1: '))
n2 = int(input('Digite número n2: '))
n3 = int(input('Digite número n3: '))

if n1 < n2 & n3:
    print(f'N1 = {n1} É o menor número')
elif n2 < n1 & n3:
    print(f'N2 = {n2} É o menor número')
else:
    print(f'N3 = {n3} É o menor número')
    