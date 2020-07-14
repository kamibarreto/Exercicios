salario = float(input('Digite qual o seu salario: '))
dez = (salario * 0.10) + salario
qui = (salario * 0.15) + salario
if salario <= 1250:
    print('Seu salario terá um aumento de 15%, sendo assim ficará R${:.2f}'.format(qui))
else:
    print('Seu salario terá um aumento de 10%, sendo assim ficará R${:.2f}'.format(dez))