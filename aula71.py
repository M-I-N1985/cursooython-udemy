''' Iteraveis, iteradores e geradores '''

lista = [0,1,2,3,4,5]
string = 'String'

print("verificando se o item é iterável")
print(hasattr(lista, '__iter__'))
print(hasattr(string, '__iter__'))

print("verificando se o item é um iterador")
print(hasattr(lista,'__next__'))

print('o for usa a função iter')
lista = iter(lista)
print(hasattr(lista, '__next__'))

print('o que acontece agora?')
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))

print('sobre geradores')

import sys
import time

print('Abaixo foi importado a função sleep para simular uma demora para processar')
print('Foi mostrado abaixo que o iterador faz tudo de uma vez só')
def gera():
    r= []
    for n in range(25):
        r.append(n)
        time.sleep(0.1)
    return r
g = gera()

for v in g:
    print(v)

print('')
print('Aqui é mostrado que o iterador faz um por vez')

def gera():
    for n in range(25):
        yield n
        time.sleep(0.1)

g = gera()

for v in g:
    print(v)

print('')
print('geradores são iteradores e iteraveis')
print(hasattr(g, '__iter__'))
print(hasattr(g, '__next__'))
print()
print()
print('ex2')
def gera():
    variavel = 'Valor 1'
    yield variavel
    variavel = 'Valor 2'
    yield variavel
    variavel = 'Valor 3'
    yield variavel

g = gera()

print(next(g))
print(next(g))
print(next(g))
#print(next(g))

g = gera()

print()
print('igual ao exemplo acima, porém usado "for"')
for v in g:
    print(v)

print()
print('outro exemplo')

lista = list(range(1000))
lista2 = [ x for x in range(1000)]
lista3 = (x for x in range(1000))
print(type(lista))
print(type(lista2))
print(type(lista3))

print('para verificar o tamanho da variavel')
print(sys.getsizeof(lista))
print(sys.getsizeof(lista2))
print(sys.getsizeof(lista3))
print()

lista = list(range(100000))
lista2 = [x for x in range(100000)]
lista3 = (x for x in range(100000))
print(sys.getsizeof(lista))
print(sys.getsizeof(lista2))
print(sys.getsizeof(lista3))


