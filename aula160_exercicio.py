import copy

from aula160_dados_exercicio import produtos


""" Aumente os preços dos produtos a seguir em 10%;
Gere novos_produtos por deep copy (cópia profunda)
"""

print('\n', 'LISTA INICIAL DE PRODUTOS:', sep='')
print(*produtos, sep='\n')

novos_produtos = [
    {**item, 'preco': round(item['preco'] * 1.1, 2)}
    for item in copy.deepcopy(produtos)
]

# for item in novos_produtos:
#     item['preco'] = item['preco'] * 1.1

print('\n', 'PREÇOS AUMENTADOS EM 10%:', sep='')
print(*novos_produtos, sep="\n")
print('\n', '######################', '\n')


""" Ordene os produtos por nome decrescente (do maior para o menor)
Gere produtos_ordenados_por_nome por deep copy
"""

produtos_ordenados_por_nome = copy.deepcopy(novos_produtos)

produtos_ordenados_por_nome.sort(key=lambda item: item['nome'])

print('PRODUTOS ORDENADOS POR NOME:')
print(*produtos_ordenados_por_nome, sep='\n')
print('\n', '######################', '\n')

""" Ordene os produtos por preço crescente (do menor para o maior)
Gere produtos_ordenados_por_preco por deep copy
"""

produtos_ordenados_por_preco = copy.deepcopy(novos_produtos)

produtos_ordenados_por_preco.sort(key=lambda item: item['preco'])

print('PRODUTOS ORDENADOS POR PREÇO:')
print(*produtos_ordenados_por_preco, sep='\n')
print('\n', '######################', '\n')