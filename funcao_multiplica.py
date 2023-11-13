def Mult(*args):
    total=1
    for numeros in args:
        total*=numeros
    return(total)

print(Mult(1,2,3,2))
