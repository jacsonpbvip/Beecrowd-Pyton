contadorPar = 0
contadorImpar = 0
contadorNegativo = 0
contadorPositivo = 0

for n in range(0, 5):

    entrada = float(input())
    if entrada < 0:
        contadorNegativo = contadorNegativo + 1
    elif entrada > 0 :
        contadorPositivo = contadorPositivo + 1    
    if entrada % 2 == 0:
        contadorPar = contadorPar + 1
    else:
        contadorImpar = contadorImpar + 1

print(f'{contadorPar} valor(es) par(es)')
print(f'{contadorImpar} valor(es) impar(es)')
print(f'{contadorPositivo} valor(es) positivo(s)')
print(f'{contadorNegativo} valor(es) negativo(s)')