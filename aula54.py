"""
1 - Crie uma função que exibe uma saudação com paramentros saudação e nome.
"""
def saudacao(saudacao, nome):
    print(f'{saudacao} {nome}')

saudacao('Olá', "Iuri")
saudacao('Oi', 'Taina')
saudacao('Bom dia', 'seu jumento')


"""
2 - Crie uma função que recebe 3 numeros como parametros e exiba a soma entre eles. 
"""
def soma(num1, num2, num3):
   print(num1 + num2 + num3)

soma(3, 5, 8)
soma(1, 2, 3)
soma(3, 6, 9)

"""
3 - Crie uma função que receba 2 numeros. O primeiro é um valor o segundo um percentual (Ex. 10%). 
Retorne o valor do primeiro numero somado ao ao aumento do percentual do mesmo.    
"""
def variacao(valor, percentual):
    return valor + percentual * valor

aumento_percentual = variacao(100, 0.10)
print(aumento_percentual)
aumento_percentual = variacao(70, 0.15)
print(aumento_percentual)
aumento_percentual = variacao(50, 0.25)
print(aumento_percentual)

"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 2, retorne fizz, se o parametro da função for divisivel por 5, retorne buzz.
Se o parametro da função for divisivel por 5 e por 3, retorne FizzBuzz, caso contrário, retorno o numero enviado.
"""

# def divisivel(num):
#     if (num % 15 == 0):
#         return "FizzBuzz"
#     elif num % 5 == 0:
#         return "Buzz"
#     elif num % 3 == 0:
#         return "Fizz"
#     else:
#         return num
def divisivel(num):
    if num % 3 == 0 and num % 5 == 0:
        return f'FizzBuzz, {num} é divisivel por 3 e 5'
    if num % 5 == 0:
        return f'Buzz, {num} é divisivel por 5'
    if num % 3 == 0:
        return f'Fizz, {num} é divisivel por 3'
    return num

from random import randint

for i in range(10):
    n = randint(0,100)
    print(divisivel(n))

