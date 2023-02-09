from aula81 import produtos, pessoas, lista
from functools import reduce

soma_lista = reduce(lambda ac, i: ac + i, lista,0)
print(soma_lista)

print('forma alternativa')
i = 0
for numero in lista:
    i += numero
soma_lista2 = i
print(soma_lista2)
print()

soma_preco = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print(soma_preco)

soma_idade = reduce(lambda ac, p: ac + p['idade'], pessoas, 0)
media_idade = soma_idade/len(pessoas)
print(media_idade)