perguntas = {
    'Pegunta1': {
        'pergunta' : 'Quanto é 2 + 2?',
        'resposta' : {'a': '1', 'b': '4', 'c' : '5'},
        'resposta_certa' : 'b',
    },

    'Pegunta2': {
        'pergunta' : 'Quanto é 3 * 2?',
        'resposta' : {'a': '3', 'b': '4', 'c' : '6'},
        'resposta_certa' : 'c',
    },

    'Pegunta3': {
        'pergunta' : 'Quanto é 5 + 5?',
        'resposta' : {'a': '10', 'b': '4', 'c' : '6'},
        'resposta_certa' : 'a',
    },
    'Pegunta4': {
        'pergunta' : 'Quanto é 2 * 2?',
        'resposta' : {'a': '3', 'b': '4', 'c' : '6'},
        'resposta_certa' : 'b',
    },
}
print('[TEXTO EXPLICATIVO]')

resposta_certa = 0
for question_main, question in perguntas.items():
    print(f'{question_main} -> {question["pergunta"]}')

    for opcao_resposta, valor_resposta in question['resposta'].items():
        print(f'{[opcao_resposta]} : {valor_resposta}')

    opc = str(input("Qual é a sua opção?"))

    if opc == question['resposta_certa']:
        print('Você acertou!!!')
        resposta_certa += 1
    else:
        print('Você errou...')

quantidade_perguntas = len(perguntas)
porcentagem_de_acerto =  resposta_certa / quantidade_perguntas * 100
print(f'Voccê acertou {resposta_certa}')
print(f'A sua porcentagem de acertou foi de {porcentagem_de_acerto}%')