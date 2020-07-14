cid = str(input('Digite o nome da cidade: ')).strip()
m = cid[0:5]
n = 'SANTO' in m.upper()
print('Sua cidade inica com santo? {}'.format(n))
