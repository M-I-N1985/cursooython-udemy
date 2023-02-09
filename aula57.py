# variavel = 'valor'

# def func():
#     print(variavel)
#
# def func2():
#     variavel = 'Outro valor'
#     print(variavel)

#-------------------------------------------------------

# def func():
#     print(variavel)
#
# def func2():
#     global variavel
#     variavel = 'Outro valor'
#     print(variavel)
#
# func()
# func2()
# print(variavel)

#-------------------------------------------------------
# variavel = 'valor'

# def func():
#     print(variavel)
#
# def func2(arg=None):
#     arg = arg.replace('v', 'c')
#     return arg
#
# func()
# outra_variavel = func2(arg = variavel)
# print(outra_variavel)

#-------------------------------------------------------
variavel = 'valor'

def func():
    outra_variavel = 'Iuri Mesquita Nunes'
    return outra_variavel

def func2(arg):
   print(arg)

var = func()
func2(var)
