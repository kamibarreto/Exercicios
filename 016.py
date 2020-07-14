from math import floor, trunc
n = float(input('Digite um numero real: '))
r = floor(n)
print('o numero real de {} é {}'.format(n, r))

#outro metodo, e o correto é:

n2 = float(input("Digite outro numero real: "))
r2 = trunc(n2)
print("o numero real de {} é {}".format(n2, r2))

#outro metodo tambem

n3 = float(input('Digite um numero real: '))
print("o numero real de {} é {}".format(n3, int(n3)))

#outro e outro metodo

n4 = float(input('Digite um numero real: '))
print("o numero real de {} é {:.0f}".format(n4, n4))

#nesse ultimo ele arredonda