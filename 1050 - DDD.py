ddd = {61: 'Brasilia', 71: 'Salvador', 11: 'Sao Paulo', 21: 'Rio de Janeiro',
       32: 'Juiz de Fora', 19: 'Campinas', 27: 'Vitoria', 31: 'Belo Horizonte'}

entrada = int(input())

if entrada == 61 or entrada == 71 or entrada == 11 or entrada == 21 or entrada == 32 or entrada == 19 or entrada == 27 or entrada == 31:
    print(ddd[entrada])
else:
    print('DDD nao cadastrado')