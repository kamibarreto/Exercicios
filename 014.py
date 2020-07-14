temp = float(input('Digite a temperatura em Graus: '))
f = (temp * 1.8) + 32
k = temp + 273.15
print('{:.2f}ºC em Fahrenheit é {:.2f}ºF, e em Kelvin é {:.2f}ºk'.format(temp, f, k))