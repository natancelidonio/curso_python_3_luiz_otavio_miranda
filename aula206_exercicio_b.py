""" Exercício - Salve sua classe em JSON
Salve os dados da sua classe em JSON
e depois crie novamente as instâncias
da classe com os dados salvos
Faça em arquivos separados.
"""

import json

class Pessoa:
    def __init__(self, nome, idade, profissao, estado_civil):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        self.estado_civil = estado_civil

with open('aula206_exercicio_a.json', 'r', encoding='utf8') as banco_dados:
    dados = json.load(banco_dados)

pessoa = Pessoa(**dados)

print(pessoa.__dict__)