"""
Funções - def em Python (parte 1)
"""
# def funcao():
#     print('Oi!!')
#
# funcao()
# -------------------------
def saudacao(msg, nome):
    print(msg, nome)

saudacao('olá', 'Iuri')
saudacao('Hello', 'world')

def saudacao(msg='olá', nome='Iuri'):
    print(msg, nome)

saudacao()
saudacao('Hello', 'world')
saudacao('oi')
saudacao(nome='João', msg='Hello')

def saudacao(msg='olá', nome='Usuário'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    return f'{msg} {nome}'
variavel = saudacao()
print(variavel)



