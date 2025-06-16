""" Exercício - salvar a lista de tarefas em um arquivo JSON e recupera-la para listar os dados.
"""

import json


caminho = 'aula195_exercicio_db.json'

def salvar_db(lista):
    with open(caminho, 'w', encoding='utf8') as db_tarefas:
        json.dump(lista, db_tarefas)

def ler_db():
    dados = []
    with open(caminho, 'r', encoding='utf8') as db_tarefas:
        dados = json.load(db_tarefas)
    return dados

tarefas = list(ler_db())
memoria = []

def listar(lista):
    print('TAREFAS:\n')
    print(*lista, sep='\n')
    print()

def desfazer(lista):
    if len(lista) == 0:
        print('Nada a desfazer.\n')
    else:
        memoria.append(lista[-1])
        lista.pop()
        salvar_db(lista)
    
def refazer(lista):
    if len(memoria) == 0:
        print('Nada a refazer.\n')
    else:
        lista.append(memoria[-1])
        memoria.pop()
        salvar_db(lista)



while True:
    print('Comandos: listar, desfazer, refazer')
    acao = input('Digite uma tarefa ou comando: ')
    print()
    
    match acao:
        case 'listar':
            listar(tarefas)
        case 'desfazer':
            desfazer(tarefas)
        case 'refazer':
            refazer(tarefas)
        case 'sair':
            print('Encerrando o programa. Até a próxima!\n')
            break
        case 'parar':
            print('Encerrando o programa. Até a próxima!\n')
            break
        case other:
            tarefas.append(acao)
            salvar_db(tarefas)