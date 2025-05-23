# Exercício - Calculo do primeiro dígito do CPF

cpf = input('Digite um CPF (sem ponto e sem traço): ')
nove_digitos = cpf[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1

primeiro_digito = (resultado_digito_1 * 10) % 11
print(primeiro_digito if primeiro_digito <= 9 else 0)

contador_regressivo_2 = 11
resultado_digito_2 = 0

for digito in nove_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1

resultado_digito_2 += primeiro_digito * contador_regressivo_2
segundo_digito = (resultado_digito_2 * 10) % 11

print(segundo_digito if segundo_digito <= 9 else 0)

print(f'{nove_digitos}-{primeiro_digito}{segundo_digito}')