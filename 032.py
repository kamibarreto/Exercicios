n = int(input('Digite o ano: '))
pri = n % 4
if pri == 0:
    n1 = n % 100
    if n1 == 0:
        ter = n % 400
        if ter == 0:
            print('É um ano bissexto')
        else:
            print('Não é bissexto')
    else:
        print('É um ano bissexto')
else:
    print('Não é bissexto')
