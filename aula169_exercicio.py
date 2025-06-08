""" Exercício - Unir listas
Crie uma função zipper (como o zipper de roupas)
O trabalho dessa função será unir duas listas na ordem.
Use todos os valores da menor lista.
Ex.:
['Salvador', 'Ubatuba', 'Belo Horizonte']
['BA', 'SP', 'MG', 'RJ']
Resultado:
[('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
"""

cidades_lista = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados_lista = ['BA', 'SP', 'MG', 'RJ']

def zipper(lista1, lista2):
    return [
        (lista1[i], lista2[i]) for i in range(min(len(lista1), len(lista2)))        
    ]

print(zipper(cidades_lista, estados_lista))