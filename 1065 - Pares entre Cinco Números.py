contador = 0

for n in range(0, 5):

    entrada = float(input())

    if entrada % 2 == 0:
        contador = contador + 1   

print(f'{contador} valores pares')