nome = input('Qual é seu nome?')
if nome.isdigit():
    print('Isso não é um nome')
else:
    if len(nome)<=4 :
        print(f'{nome}: Nome curto')
    elif len(nome)==5 or len(nome)==6 :
        print(f'{nome}: Nome normal')
    else:
        print(f'{nome}: Nome muito grande')