#Exercícios

# numero = input('Digite um número inteiro: ')

# if numero.isdigit():
#     if int(numero) % 2 != 0:
#         print('Esse número é ímpar')
#     else:
#         print('Esse número é par')
# else:
#     print('Você não digitou um número inteiro.')

############################################################


# hora = int(input('Qual é a hora? '))

# manha = hora >= 0 and hora <= 11
# tarde = hora >= 12 and hora <= 17
# noite = hora >= 18 and hora <= 23

# if manha:
#     print('Bom dia!')
# elif tarde:
#     print('Boa tarde!')
# elif noite:
#     print('Boa noite!')


############################################################


nome = input('Qual é seu primeiro nome? ')
tamanho_nome = len(nome)

nome_curto = tamanho_nome <= 4
nome_normal = tamanho_nome == 5 or tamanho_nome == 6
nome_longo = tamanho_nome > 6

if nome_curto:
    print('Seu nome é curto.')
elif nome_normal:
    print('Seu nome é normal.')
elif nome_longo:
    print('Seu nome é muito grande!')