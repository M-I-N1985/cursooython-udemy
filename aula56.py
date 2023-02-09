"""
Funções (def) em Python - *args **kwargs -
Aula 16 (parte 3)
- para a variável retornar um valor, tem que colocoar return,
pois se deixar somente com o comando print, essa variavel será uma variavel None

*args = o asterisco indica um argumento e a nomeclatura args é utilizada pela comunidade por convenção, podendo ser qualquer outra.
**kwargs = o asterisco duplo indica uma kwargs
"""

# def func(a1, a2, a3, a4, a5, nome = None, a6 = None):
#     print(a1, a2, a3, a4, a5, nome, a6)
#
# var = func(1,2,3,4,5, nome = 'Iuri', a6 = '5')
# print(var)
#-----------------------------------------------------------------------

# def func(a1, a2, a3, a4, a5, nome = None, a6 = None):
#     print(a1, a2, a3, a4, a5, nome, a6)
#     return nome, a6
#
# var = func(1,2,3,4,5, nome = 'Iuri', a6 = '5')
# print(var[0], var[1]    )
#-----------------------------------------------------------------------

# def func(*args):
#     print(args)
#     print(args[0])
#     print(args[-1])
#     print(len(args))

# lista = [1,2,3,4,5]
# n1, n2, *n = lista
# print(n1, n2, n)
#
# lista = [1,2,3,4,5]
# print(*lista)
# print(*lista, sep = '-')

# func(1,2,3,4,5)

#-----------------------------------------------------------------------

#como args retorna uma tupla, não é possível alterá-la, tendo que fazer um casting para list
# def func(*args):
#     args = list(args)
#     args[0] = 20
#     print(args)
#
#
# func(1,2,3,4,5)
#-----------------------------------------------------------------------

# def func(*args):
#     for v in args:
#         print(v)
#
#
# func(1,2,3,4,5)

#-----------------------------------------------------------------------

# def func(*args):
#     print(args)
#
# lista = [1,2,3,4,5]
# lista2 = [10,20,30,40,50]
# func(lista, 6)
# func(*lista, 6)
# func(*lista, *lista2)

#-----------------------------------------------------------------------

#kwargs faz o args para argumentos nomeados
# def func(*args, **kwargs):
#     print(args)
#     print(kwargs)
#     print(kwargs['nome'], kwargs['sobrenome'])
#
# lista = [1,2,3,4,5]
# lista2 = [10,20,30,40,50]
# func(*lista, *lista2, nome='Iuri', sobrenome = 'Nunes')
#-----------------------------------------------------------------------

# def func(*args, **kwargs):
#     print(args)
#     nome = kwargs.get('nome')
#     print(nome)
#
# lista = [1,2,3,4,5]
# lista2 = [10,20,30,40,50]
# func(*lista, *lista2, nome='Iuri', sobrenome = 'Nunes')
#-----------------------------------------------------------------------

def func(*args, **kwargs):
    print(args)
    idade = kwargs.get('idade')
    print(idade)
    # if idade is not None:
    #     print(idade)

lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]
func(*lista, *lista2, nome='Iuri', sobrenome = 'Nunes')
# func(*lista, *lista2, nome='Iuri', sobrenome = 'Nunes', idade=36)