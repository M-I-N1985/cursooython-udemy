"""
Zip - Unindo iteráveis
Zip_longest - Itertools
"""

from itertools import zip_longest, count


### código
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados = ['SP', 'MG', 'BA']

cidades_estados = zip(cidades, estados)
# print(next(cidades_estados))
# print(next(cidades_estados))
# print(next(cidades_estados))

for valor in cidades_estados:
    print(valor)

cidades_estados = zip(estados, cidades)
print(cidades_estados)
print(list(cidades_estados))
# print(dict(cidades_estados))

print()
print('Exemplo abaixo com zip_longest')
indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'Outra']
estados = ['SP', 'MG', 'BA']

cidades_estados = zip_longest(estados, cidades, fillvalue = 'Estado')
print(list(cidades_estados))

cidades_estados = zip(indice, estados, cidades)

for indice, estados, cidades in cidades_estados:
    print(indice, estados, cidades)
