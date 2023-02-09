""" Exemplo de dicionário comprehension"""

lista = [('chave', 'valor'), ('chave1', 'valor1')]
d = dict(lista)
print(d)

d1 = { x: y for x,y in lista}
print(d1)

d2 = { x: y*2 for x, y in lista}
print(d2)

d3 = { x: y for x, y in enumerate(range(5))}
print(d3)

print("")
print("no exemplo abaixo, não seria possivel fazer isso com uma função dict")
d4 = { x.upper(): y.upper() for x, y in lista}
print(d4)

d5 = {f'chave{x}': x**2 for x in range(5)}
print(d5)
