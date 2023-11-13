import os
lista=[]
contador=0
while True :
    opcao=input("[A]dicionar [R]emover [L]istar  ").lower()
    if opcao == 'a':
        os.system('cls')
        produto = input('O que deseja adicionar? ')
        lista.append(produto)
        contador=1
    elif opcao == 'r' :
        os.system('cls')
        if contador==0:
            print('Nenhum produto para remover')
        else:
            for indice, item in enumerate(lista):
                print(indice,item)
            try:
                remove=int(input('Digite o codigo para remoção do item: '))
                del lista[remove]
            except ValueError : 
                print('Por favor digite apenas números inteiros')
            except IndexError :
                print('Esse indice não existe')
            
    elif opcao == 'l':
        os.system('cls')
        if contador==0:
            print('Nenhum produto para listar')
        else:
            for indice,item in enumerate(lista):
                    print(indice,item)
                
    else:
        os.system('cls')
        print('O programa foi encerrado!')
        break
        
    


