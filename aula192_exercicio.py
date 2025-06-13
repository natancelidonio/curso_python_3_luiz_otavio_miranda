""" Exercício - Lista de tarefas com desfazer e refazer
"""

todo = []
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
    
def refazer(lista):
    if len(memoria) == 0:
        print('Nada a refazer.\n')
    else:
        lista.append(memoria[-1])
        memoria.pop()



while True:
    print('Comandos: listar, desfazer, refazer')
    acao = input('Digite uma tarefa ou comando: ')
    print()
    
    match acao:
        case 'listar':
            listar(todo)
        case 'desfazer':
            desfazer(todo)
        case 'refazer':
            refazer(todo)
        case 'sair':
            print('Encerrando o programa. Até a próxima!\n')
            break
        case 'parar':
            print('Encerrando o programa. Até a próxima!\n')
            break
        case other:
            todo.append(acao)