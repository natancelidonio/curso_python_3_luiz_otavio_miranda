import json

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numero_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

with open('aula190.json', 'w', encoding='utf8') as arquivo:
    json.dump(pessoa, arquivo, ensure_ascii=False, indent=2)

### IMPORTANDO DADOS DE VOLTA DO ARQUIVO JSON

# with open('aula190.json', 'r', encoding='utf8') as arquivo:
#     pessoa = json.load(arquivo)
#     print(pessoa)