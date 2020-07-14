from math import hypot
cat1 = float(input('Digite o cateto oposto: '))
cat2 = float(input('Digite o cateto adjacente: '))
n = hypot(cat1, cat2)
print("a hipotenusa é igual á: {:.2f}".format(n))
n2 = (cat1 ** 2 + cat2 **2) ** (1/2)
print("a hiptotenusa é igual á: {:.2f}".format(n2))
