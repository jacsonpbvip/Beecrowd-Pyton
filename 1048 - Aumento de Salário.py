salario = float(input())

newSalario = 0
reajuste = 0
aumento = 0
novoSalario = 0

if salario > 0 and salario <= 400:
    reajuste = (salario / 100) * 15
    novoSalario = reajuste + salario
    aumento = 15

elif salario >= 400.01 and salario <= 800:
    reajuste = (salario / 100) * 12
    novoSalario = reajuste + salario
    aumento = 12

elif salario >= 800.01 and salario <= 1200:
    reajuste = (salario / 100) * 10
    novoSalario = reajuste + salario
    aumento = 10

elif salario >= 1200.01 and salario <= 2000:
    reajuste = (salario / 100) * 7
    novoSalario = reajuste + salario
    aumento = 7

elif salario > 2000:
    reajuste = (salario / 100) * 4
    novoSalario = reajuste + salario
    aumento = 4

print(f"Novo salario: {novoSalario:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {aumento} %")