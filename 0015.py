dias = float(input('Quantos dias alugados: '))
km = float(input('Quantos KM percorrido: '))
valor = (km * 0.15 ) + (dias * 60)
print('O valor a pagar é {:.2f}'.format(valor))
