numero= input("Digite um numero inteiro: ")
if numero.isdigit():

    numero_int=int(numero)
    if(numero_int // 1 == numero_int) :
        if (numero_int % 2 == 0) :
            print(f'o número {numero_int} é par')
        else: print(f'o número {numero_int} ímpar')
else:
    print('Isso não é um número ou é um número Decimal !')