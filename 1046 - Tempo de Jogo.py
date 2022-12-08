a, b = str(input()).split()

a = int(a)
b = int(b)
tempo = 0

if a < b:
    tempo = b - a
else:
    tempo = (24 - a) +b

print(f"O JOGO DUROU {tempo} HORA(S)")