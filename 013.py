salario = float(input('Digite o salario do funcionario: R$'))
porce = salario * 0.15
aumento = salario + porce
print('O salario atual do funcionario é R${:.2f}, com um aumento de 15% fica R${:.2f}'.format(salario, aumento))
print('Ele teve um aumento de R${:.2f}'.format(porce))
