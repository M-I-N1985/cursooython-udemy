'''
count - itertools
'''

from types import GeneratorType
variavel = zip('Alo', 'Alo')
print(list(variavel))
print()

print('entendendo melhor!')
variavel = zip('Alo', 'Alo')
print(next(variavel))
print(next(variavel))
print(next(variavel))
print(isinstance(variavel, GeneratorType))
print()

print('exemplo de gerador')
variavel = ((x,y) for x, y in zip('Alo', 'Alo'))
print(isinstance(variavel, GeneratorType))
print(list(variavel))
print()

from itertools import count

contador = count(start=5, step=2)
print(next(contador))
print(next(contador))
print(next(contador))
print()
for valor in contador:
    print(valor)

    if valor >= 13:
        break
print()

print('exemplo com casas decimais e arredondadmeto')

contador = count(start=5, step=0.15)

for valor in contador:
    print(round(valor, 2))

    if valor >= 13:
        break
print()

print('colocando indices')

contador = count()
lista = ['Luis', 'João', 'Maria']
lista = zip(contador, lista)
print(list(lista))


