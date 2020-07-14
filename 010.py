n = float(input('Digite o quanto você tem na carteira: R$'))
dolar = n / 5.36
euro = n / 6.07
print('Em sua carteira tem R${}, e isso em dolar é ${:.2f} e eu em euro é €{:.2f}'.format(n, dolar, euro))