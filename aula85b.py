print('Levantando minha propria exceção')
print('_________________________________________________________')

def divide2(n1, n2):
    if n2 == 0:
        raise ValueError('n2 não pode ser 0')
print(divide2(2,0))