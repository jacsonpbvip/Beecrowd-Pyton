contador = 0
soma = 0
for n in range(0, 6):

    entrada = float(input())

    if entrada >= 0:
        contador = contador + 1
        soma = soma + entrada
media = soma / contador

print(f'{contador} valores positivos')
print(f'{media:.1f}')