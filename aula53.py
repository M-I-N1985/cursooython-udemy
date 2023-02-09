"""
Funções (def) em Python - return - aula 16 (parte 2)
"""

# def funcao(var):
#     print(var)
#
# variavel = funcao('Valor que eu quero')
#
# if variavel:
#     print(variavel)
# else:
#     print('nenhum')
#------------------------------------------
# def funcao(var):
#     print('isso não será executado!')
#     return var
#
# variavel = funcao('Valor que eu quero')
#
# if variavel:
#     print(variavel)
# else:
#     print('nenhum')
# -----------------------------------
# def divisao(n1, n2):
#     if n2 > 0:
#         return n1/n2
#
# divide = divisao(8, 2)
#
# if divide:
#     print(divide)
# else:
# #     print('Conta inválida')
# ---------------------------------------
# def divisao(n1, n2):
#     if n2 == 0:
#         return
#     return n1/n2
#
# divide = divisao(8, 0)
#
# if divide:
#     print(divide)
# else:
#     print('Conta inválida')
#-----------------------------------
# def dumb():
#     return
# var = dumb()
# print(var, type(var))
#-----------------------------------
# def f(var):
#     print(var)
#
# def dumb():
#     return f
#
# print(type(f))
#
# var = dumb()
# print(id(var), id(f))
#
# if var == f:
#     print('var é igual a f')
# else:
#     print('Blaaa')
#-----------------------------------
def dumb():
    return 'Iuri', 'Nunes'
print(dumb(), type(dumb()))

def dumb():
    return ('Iuri', 'Nunes')
print(dumb(), type(dumb()))
