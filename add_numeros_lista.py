pares=[]
impares=[]
i=0
while i <= 10:
    if i%2 == 0:
        pares.append(i)
        
    else:
        impares.append(i)
        
    i+=1
print(f"Pares: {pares}")
print(f"Pares: {impares}")
