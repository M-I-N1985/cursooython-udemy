"""
For / Else em Python
"""

variavel = ['Iuri', 'Joãozinho', 'Maria']

# for valor in variavel:
#     if valor.startswith('J'):
#         print('Começa com J:', valor)
#     else:
#         print('Não começa com J:', valor)

# __________________________________________________________

# comeca_com_j = False
# for valor in variavel:
#     if valor.lower().startswith('j'):
#         comeca_com_j = True
#
# if comeca_com_j:
#     print('Existe uma palavra que começa com J.')
# else:
#     print('Não existe uma palavra que começa com J.')

# __________________________________________________________


for valor in variavel:
    print(valor)
    if valor.lower().startswith('j'):
        break
else:
    print('Não existe uma palavra que começa com J.')
