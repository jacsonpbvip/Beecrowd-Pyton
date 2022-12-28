contador = 0
for n in range(0, 6):
    
    entrada = float(input())

    if entrada > 0:
        contador = contador + 1

print(f'{contador} valores positivos')