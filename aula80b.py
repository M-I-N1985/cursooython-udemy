from itertools import groupby, tee

# tee faz copia de iteradores, copy faz cópia de iteraveis


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


for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados)

    print(f'agrupamento:{agrupamento}')

    for aluno in va1:
        print(f't{aluno}')
    quantidade = len(list(va2))
    print(f'\t{quantidade} alunos tiraram a nota {agrupamento}')
print()
