# tratando numeros com ponto flutuantes, e letras

def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError as erro:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass


while True:
    numero = converte_numero(input('Digite um número: '))
    if numero is not None:
        print(numero * 5)
    else:
        print('Isso não é numero!')


print(numero*5)
