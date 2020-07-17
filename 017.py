'''from math import hypot
cat1 = float(input('Digite o cateto oposto: '))
cat2 = float(input('Digite o cateto adjacente: '))
n = hypot(cat1, cat2)
print("a hipotenusa é igual á: {:.2f}".format(n))
n2 = (cat1 ** 2 + cat2 **2) ** (1/2)
print("a hiptotenusa é igual á: {:.2f}".format(n2))'''
from math import hypot
a = float (input('Digite o valor do cateto oposto '))
b = float (input('Digite o valor do cateto adjacente '))
d = a * 2
e = b * 2
f = d + e
c = f ** (1/2)
print('{}'.format(c))
