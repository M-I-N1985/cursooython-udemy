"""
Combinations, Permutations e Product - Itertools
Combinação - Ordem não importa
Permutação - ordem importa
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos

"""

from itertools import combinations, permutations, product

pessoas = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']

print('exemplo de combinação')
for grupo in combinations(pessoas, 2):
    print(grupo)
print()

print('exemplo de permutação')
for grupo in permutations(pessoas, 2):
    print(grupo)
print()

print('exemplo de produto')
for grupo in product(pessoas, repeat=2):
    print(grupo)
print()