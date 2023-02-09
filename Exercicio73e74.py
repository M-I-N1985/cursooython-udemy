carrinho = []

carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 20))
carrinho.append(('Produto 3', 50))

print(carrinho)

print()
print("Exemplo ineficaz 1 do professor")

total = 0
for produto in carrinho:
    total += produto[1]
print(total)

print()
print("Exemplo ineficaz 2 do professor")

total = []
for produto in carrinho:
    total.append(produto[1])
print(total)
print(sum(total))

print()
print("o que eu fiz")

total = sum([produto[1] for produto in carrinho])
print(total)

print()
print("solução do professor")

total = sum([float(y) for x, y in carrinho])
print(carrinho)
print(total)

