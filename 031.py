n = float(input('Digite a quilometragem viajada: '))
cur = 0.50 * n
lon = 0.45 * n
if n <= 200:
    print('O valor a se pagar pela viagem é de R${:.2f}'.format(cur))
else:
    print('O valor a se pagar pela viagem é de R${:.2f}'.format(lon))
print('ANTENÇÃO: Lembrando que cobramos R$0.50 centavos por KM para viagens ate 200KM')
print('          Acima desta quilometragem, a cobrança sera de R$0.45 a cada KM')
