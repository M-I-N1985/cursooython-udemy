"""
Considerando duas listas de interiros ou floats (lista A e lista B)
some os valores nas listas retornando uma nova lista com os valores somados:

Se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor

Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]

=====================================  resultado
lista_soma  =   [2, 4, 6, 8]
"""
from itertools import zip_longest

lista_a= [1, 2, 3, 4, 5, 6, 7]
lista_b= [1, 2, 3, 4]
print()
print('minha resolução')
lista_ab = list(zip(lista_a, lista_b))
lista_soma = [x + y for x, y in lista_ab]
print(lista_soma)
print()

print('resoluções do professor')
lista_a= [1, 2, 3, 4, 5, 6, 7]
lista_b= [1, 2, 3, 4]

lista_soma = []
for i in range(len(lista_b)):
    lista_soma.append(lista_a[i] + lista_b[i])
print(lista_soma)

lista_a= [1, 2, 3, 4, 5, 6, 7]
lista_b= [1, 2, 3, 4]
print_soma = [x + y for x,y in zip(lista_a, lista_b)]
print(lista_soma)
print()

print('Outro exemplo oferecido pelo professor para caso onde eu não queira excluir os numeros restantes da lista maior, e sim inclui-lo')

lista_a = [10, 2, 3, 4, 5]
lista_b = [12, 2, 3, 6, 50, 60, 70]
lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
print(lista_soma)
