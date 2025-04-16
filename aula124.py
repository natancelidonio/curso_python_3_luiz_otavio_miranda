# Exercícios - sistemas de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

contador_acertos = 0

for item in perguntas:
    print(f'Pergunta: {item['Pergunta']}\n')
    
    print(f'Opções:')
    opcoes = item['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i}) {opcao}')
    print()
    
    resposta_int = None
    qtd_opcoes = len(opcoes)
    
    resposta = input('Digite o n° da opção como resposta: ')
    if resposta.isdigit():
        resposta_int = int(resposta)
    else: 
        print('\n❌ Resposta errada.\n')
        
    if resposta_int is not None:
        if resposta_int >= 0 and resposta_int < qtd_opcoes:
            if opcoes[resposta_int] == item['Resposta']:
                print('\n✅ Resposta certa!\n')
                contador_acertos += 1
            else:
                print('\n❌ Resposta errada.\n')
        else:
            print('\n❌ Resposta errada.\n')
            
print(f'Você acertou {contador_acertos} de {len(perguntas)}.')


