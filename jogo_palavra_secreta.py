import os
continuar = input('Deseja adicionar uma nova palavra secreta? [S]im ou [N]ão\t').lower()
if continuar == 's':
    palavra_secreta = input('Digite a palavra secreta ')
    letras_acertadas = ''
    numero_tentativas = 0
    while continuar == 's':
        
        letra_digitada = input('Digite uma letra: ')
        numero_tentativas += 1
    
        if len(letra_digitada) > 1:
            print('Digite apenas uma letra.')
            continue
    
        if letra_digitada in palavra_secreta:
            letras_acertadas += letra_digitada
    
        palavra_formada = ''
        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_acertadas:
                palavra_formada += letra_secreta
            else:
                palavra_formada += '*'
    
        print('Palavra formada:', palavra_formada)
    
        if palavra_formada == palavra_secreta:
            os.system('clear')
            print('VOCÊ GANHOU!! PARABÉNS!')
            print('A palavra era', palavra_secreta)
            print('Tentativas:', numero_tentativas)
            letras_acertadas = ''
            numero_tentativas = 0
            continuar = input('Deseja adicionar uma nova palavra secreta? [S]im ou [N]ão\t').lower()
            if continuar == 'n':
                print("Fim das tentativas")
            else:
                palavra_secreta = input('Digite a palavra secreta\t')
else:
    print("Fim das tentativas")

        