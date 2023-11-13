def teste(**dados):
    for key,value in dados.items():
        print(f"{key}  - {value}")
teste(nome=input("Digite seu nome:"),idade=input("Digite sua idade:"))
# é parecido com a struct em C