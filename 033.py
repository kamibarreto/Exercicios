n = int(input('Digite um numero: '))
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
lis = [n, n1, n2]
orde = sorted(lis)
print('O menor numero é o {}'.format(orde[0]))
print('O maior numero é o {}'.format(orde[2]))
