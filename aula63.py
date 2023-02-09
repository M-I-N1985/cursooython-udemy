perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2 + 2?',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '5'},
        'resposta_certa': 'b'
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3 - 2?',
        'respostas': {'a': '1','b': '2','c': '4'},
        'resposta_certa': 'a'
    },

    'Pergunta 3': {
        'pergunta': 'Quanto é 12 / 3?',
        'respostas': {'a': '4','b': '3','c': '7'},
        'resposta_certa': 'a'
    },

    'Pergunta 4': {
        'pergunta': 'Quanto é 5 * 4?',
        'respostas': {'a': '24','b': '20','c': '22'},
        'resposta_certa': 'b'}
}

print()
resposta_certa = 0
for pk, pv in perguntas.items():
    print(f"{pk}: {pv['pergunta']}")

    print('Respostas:')
    for rk, rv in pv['respostas'].items():
        print(f"[{rk}:] {rv}")
    print()

    resp_certa = input("digite sua resposta: ")
    if resp_certa == pv["resposta_certa"]:
        print('você acertou!')
        resposta_certa += 1
    else:
        print('você errou!')

qtide_perguntas = len(perguntas)
taxa_de_acerto = resposta_certa/qtide_perguntas*100
print()
print(f'Sua taxa de acerto foi de: {taxa_de_acerto}%')
