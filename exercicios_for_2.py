numeros = []
for x in range(0,5):
    n = int(input("escreva um valor"))
    numeros.append(n)
    print(numeros)

    soma = 0
    for i in numeros:
        soma+=i

    print("A soma dos valores é: "+str(soma))

    print("A média dos valores é: "+str(soma/len(numeros)))    