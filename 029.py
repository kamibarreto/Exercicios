vel = float(input('Qual foi a velocidade registrada: '))
mul = (vel - 80) * 7
if vel <= 80:
    print('Você não recebeu multa nenhuma.')
else:
    print('Você recebeu uma multa no valor de R${:.2f}'.format(mul))
print('Lembrando que o limite de velocidade nesta via é de 80KM.')