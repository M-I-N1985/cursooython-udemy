"""
1 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada.
"""
# def ola_mundo():
#     return 'Olá Mundo!'
#
# def mestre(funcao):
#    return funcao()
#
# executando = mestre(ola_mundo)
# print(executando)


"""
2 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada. 
Faça a função1 executar duas funções que recebam um número diferente de argumentos
"""

def fala_oi(nome):
    return f'Oi{nome}'

def func2():
    print("valor da função 2")

func1(func2())

