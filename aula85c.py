print('tratando minha propria exceção')
print('_________________________________________________________')


def divide3(n1, n2):
    if n2 == 0:
        raise ValueError('n2 não pode ser 0')
    return n1 / n2
try:
    print(divide3(n1 = 2, n2 = 0))
except ValueError as error:
    print('Você está tentando dividir por zero.')
    print('Log: ', error)