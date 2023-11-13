M=("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","X","W","Y","Z")
Palavra=input("Digite a palavra:")
Palavra_tuple=tuple(Palavra) #transformei a string em tupla pra separar as letras
contM=0
contm=0
set1=set(M) #set() para criar conjuntos a partir das tuplas  
set2=set(Palavra_tuple)
maiusculas= set1.intersection(set2) #isso serve para encontrar elementos em comum entre as tuplas
if maiusculas:
    for i in maiusculas:
        contM+=1
contm=len(Palavra_tuple)-contM
print(contM)
print(contm)
    