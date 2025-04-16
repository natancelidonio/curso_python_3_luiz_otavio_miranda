# Exercício

nome = 'Natan'

tamanho_nome = len(nome)

print(nome)
print(tamanho_nome)

novo_nome = ''

contador = 0

while contador < tamanho_nome:
    novo_nome += '*'
    novo_nome += nome[contador]
    contador += 1
    if contador == tamanho_nome:
        novo_nome += '*'
        break

print(novo_nome)
