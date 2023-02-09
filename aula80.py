from itertools import groupby


alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Iuri', 'nota': 'B'},
    {'nome': 'Ana', 'nota': 'B'},
    {'nome': 'Thaina', 'nota': 'C'},
    {'nome': 'Maria', 'nota': 'D'},
    {'nome': 'Rosilda', 'nota': 'B'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Marcelo', 'nota': 'C'},
    {'nome': 'Pedro', 'nota': 'D'},
    {'nome': 'Pedro', 'nota': 'A'},
]
for aluno in alunos:
    print(aluno)
    print()


ordena = lambda item: item['nota']
alunos.sort(key = ordena)
alunos_agrupados = groupby(alunos, ordena)


print()

for agrupado in alunos_agrupados:
    print(agrupado)
print()


print('eu fiz por mim os passos abaixo')
print(alunos_agrupados)
aa1 = dict(alunos_agrupados)
print(aa1)

print('conti...')
print('cade?') #não imprime pois o alunos agrupados já foi iterado antes

ordena = lambda item: item['nota']
alunos.sort(key = ordena)
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    print(f'agrupamento:{agrupamento}')
    for aluno in valores_agrupados:
        print(aluno)
print()


ordena = lambda item: item['nota']
alunos.sort(key = ordena)
alunos_agrupados = groupby(alunos, ordena)
for agrupamento, valores_agrupados in alunos_agrupados:
    print(f'agrupamento:{agrupamento}')
    quantidade = len(list(valores_agrupados))
    print(f'{quantidade} alunos tiraram a nota {agrupamento}')
print()
