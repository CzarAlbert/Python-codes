def fatorial(num):
    if num==1:
        return(1)
    else:
        return(num*fatorialx(num-1))

number = int(input("Digite um numero inteiro:"))
print(fatorial(number))
