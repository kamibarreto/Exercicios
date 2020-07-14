from time import sleep
dis = float(input('Qual a distancia da sua viagem em quilometros? '))
print('Você esta para começar uma viagem de {}km'.format(dis))
print('CALCULANDO....')
sleep(3)
if dis <= 200:
    preço = dis * 0.50
else:
    preço = dis * 0.45
print('E o preço da sua viagem ficará R${:.2f}'.format(preço))