from aula81 import produtos, pessoas, lista
print('O map vai aplicar uma função em cada item de uma lista de itens,'
      ' ou seja, é um for com uma chamada da função para aplicá-la a cada item da sua lista.')
print()

nova_lista = map(lambda x: x*2, lista)
print(lista)
print(nova_lista)
print(list(nova_lista))
print()

nova_lista2 = [x * 2 for x in lista]
print(lista)
print(list(nova_lista2))
print()

precos = map(lambda p: p['preco'], produtos)
for preco in precos:
    print(preco)
print()

print('Se quisessemos somar em cada um dos precos 5% mas não modificar a estrutura do dic, não é possivel fazer pelo lambda então:')

def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p

novos_produtos = map(aumenta_preco, produtos)

for produto in novos_produtos:
    print(produto)
print()

nomes = map(lambda p: p['nome'], pessoas)

for pessoa in nomes:
    print(pessoa)
