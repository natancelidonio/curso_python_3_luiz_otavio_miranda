# Exercício

palavra_secreta = 'poca'
tentativas = 0
chutes_acertados = ''

while True:
    chute = input('Digite uma letra: ')
    
    if len(chute) > 1:
        print("Digite apenas uma letra.")
        continue
    
    if chute in palavra_secreta:
        chutes_acertados += chute
    
    palavra_formada = ''
    
    for letra in palavra_secreta:
        if letra in chutes_acertados:
            palavra_formada += letra
        else:
            palavra_formada += '*'
    
    print(palavra_formada)

    tentativas += 1
    
    if palavra_formada == palavra_secreta:
        print('PARABÉNS! VOCÊ ACERTOU!')
        print(f'A palavra era: {palavra_secreta}')
        print(f'Tentativas: {tentativas}')
        print('Fim.')
        break
        
