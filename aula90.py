# Exercicio

lista = []
opcoes_validas = ['i', 'a', 'l']
indices = []

while True:
    
    print('Selecione uma opção ')
    opcao = input('[i]nserir [a]pagar [l]istar: ')   

    if opcao not in opcoes_validas:
        print('Opção inválida. Digite "i", para inserir, ou "a", para apagar, ou "l" para listar.')
        continue
    
    if opcao == 'i':
        novo_item = input('O que deseja inserir na lista? ')
        lista.append(novo_item)
        continue
    
    if opcao == 'l':
        if lista == []:
            print('Você ainda não adicionou nenhum item na lista.')
            continue
        print('Sua lista contém:')
        for item in enumerate(lista):
            i, nome = item
            print(i, nome)
        print(40 * '#')
        continue
    
    if opcao == 'a':
        indice = input('Digite o índice do item que deseja apagar: ')
        try:
            indice = int(indice)
            print('Estou apagando esse item.')
            lista.pop(indice)
        except:    
            print('Erro. A lista não contém esse índice.')
            continue
            
       
       