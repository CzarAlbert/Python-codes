def Verifica(*args):
    digito=input('Digite um numero para verificação:')
    numero=int(digito)
    if numero % 2 == 0:
        print(f'O número {numero} é par!!!')
    else:
        print(f'O número {numero} é ímpar!!!')
verificador= Verifica()
