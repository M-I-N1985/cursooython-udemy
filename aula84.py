
print('descrevendo o erro através de NameError')
print('_______________________________________')
try:
    print(a)
except NameError as erro:
    print('Erro:', erro)
print()

print('somente comentando o erro')
try:
    print(a)
except NameError as erro:
    print('Erro do desenvolvedor, fale com ele.')

print()

print('executando try, pois agora a variavel "a" existe')
print('________________________________________________')
try:
    a = []
    print(a)
except NameError as erro:
    print('Erro do desenvolvedor, fale com ele.')
print('Bora continuar...')
print()

print('comentando em uma segunda excecao pois não atende ao "try" nem ao primeiro "except"')
print('___________________________________________________________________________________')
try:
    a = []
    print(a[1])
except NameError as erro:
    print('Erro do desenvolvedor, fale com ele.')
except Exception as erro:
    print('Ocorreu um erro inesperado')
print('Bora continuar...')
print()

print('Como "except Exception" é uma excecao geral para qualquer tipo de erro, ')
print('se eu quiser destacar qual exceção tratar, como no exemplo abaixo, que havia um erro de indice')
print('e eu quero destacar que é um erro de indice eu utilizo um except antes do "except Exception"')
print('___________________________________________________________________________________')
try:
    a = []
    print(a[1])
except NameError as erro:
    print('Erro do desenvolvedor, fale com ele.')
except IndexError as erro:
    print('Erro de índice.')
except Exception as erro:
    print('Ocorreu um erro inesperado')
print('Bora continuar...')
print()

try:
    a = {}
    print(a[1])
except NameError as erro:
    print('Erro do desenvolvedor, fale com ele.')
except (IndexError, KeyError) as erro:
    print('Erro de índice ou chave.')
except Exception as erro:
    print('Ocorreu um erro inesperado')
print('Bora continuar...')
print()


print('podemos também utilizar o else para caso não haja uma erro(excecao)')
print('___________________________________________________________________')
try:
    a = {}

except NameError as erro:
    print('Erro do desenvolvedor, fale com ele.')
except (IndexError, KeyError) as erro:
    print('Erro de índice ou chave.')
except Exception as erro:
    print('Ocorreu um erro inesperado')
else:
    print('Seu código foi executado com sucesso!')
    print(a)
print('Bora continuar...')
print()

print('podemos também utilizar o "Finally" independente que haja uma excecao')
print('_____________________________________________________________________')
try:
    a = 1/0

except NameError as erro:
    print('Erro do desenvolvedor, fale com ele.')
except (IndexError, KeyError) as erro:
    print('Erro de índice ou chave.')
except Exception as erro:
    print('Ocorreu um erro inesperado')
else:
    print('Seu código foi executado com sucesso!')
    print(a)
finally:
    print('Finalmente.')

print('Bora continuar...')
print()

print('E se mesmo assim ocorrer um erro, como no exemplo abaixo?')
print('_________________________________________________________')
try:
    b = (1+2)/0
except NameError as erro:
    print('Erro do desenvolvedor, fale com ele.')
except (IndexError, KeyError) as erro:
    print('Erro de índice ou chave.')
except Exception as erro:
    print('Ocorreu um erro inesperado')
else:
    pass
finally:
    b = None


print(b)
print()

print('Então o "finally" seria uma opção de tratamento do erro')
print('_______________________________________________________')
