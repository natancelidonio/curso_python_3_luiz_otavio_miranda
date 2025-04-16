# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

# Função que duplica

numero = int(input('Digite um número: '))

# def duplicar(numero):
#     return numero * 2

# print(f'O número duplicado é: {duplicar(numero)}')

# # Função que triplica

# def triplicar(numero):
#     return numero * 3

# print(f'O número triplicado é: {triplicar(numero)}')

# # Função que quadruplica

# def quadruplicar(numero):
#     return numero * 4

# print(f'O número quadruplicado é: {quadruplicar(numero)}')

# Resolução com Closure

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(f'O número duplicado é: {duplicar(numero)}')
print(f'O número triplicado é: {triplicar(numero)}')
print(f'O número quadruplicado é: {quadruplicar(numero)}')

