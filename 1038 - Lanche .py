codico, quantidade = map(int, input().split())
preco = 0
if codico == 1:
    preco = 4.0  # cachorroQuente
elif codico == 2:
    preco = 4.5  # XSalada
elif codico == 3:
    preco = 5.0  # XBacon
elif codico == 4:
    preco = 2.0  # TorradaSimples
elif codico == 5:
    preco = 1.5  # Refrigerante


print(f"Total: R$ {preco * quantidade:.2f}")
