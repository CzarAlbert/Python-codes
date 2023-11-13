hora_atual= input('Qual é a hora atual? ')
if hora_atual.isdigit():
    verif_hora= int(hora_atual)
    if verif_hora>=0 and verif_hora<=11:
        print('Bom dia')
    elif verif_hora>=12 and verif_hora<=17:
        print('Boa tarde')
    else: print('Boa noite')

else: print('Formato de hora invalida')
    
