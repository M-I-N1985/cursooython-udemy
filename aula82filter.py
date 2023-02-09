from aula81 import produtos, pessoas, lista

print('O filter vai aplicar uma função em cada item de uma lista de itens, e retornar somente as True')
print()

nova_lista = filter(lambda x: x > 5, lista)
print(list(nova_lista))

nova_listalc = [x for x in lista if x > 5]
print(list(nova_listalc))

nova_lista = filter(lambda p: p['preco'] > 50, produtos)
for produto in nova_lista:
    print(produto)
print()

def filtra(produto):
    if produto['preco'] > 50:
        return True

nova_lista = filter(filtra, produtos)

for produto in nova_lista:
    print(produto)
