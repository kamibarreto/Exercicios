n = input('Digite algo: ')
print('O tipo primitivo é:',type(n))
print("É somente espaços?", n.isspace())
print('É maiusculo?', n.isupper())
print('É minuscula?', n.islower())
print('É um numero', n.isnumeric())
print('Tem alguma letra?', n.isalpha())
print('É um titulo?', n.istitle())

