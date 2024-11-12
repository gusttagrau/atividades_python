numeros = []
n1 = int(input("digite o primeiro numero "))
n2 = int(input("digite o segundo numero "))
n3 = int(input("digite o terceiro numero "))
# adicionar os numeros a lista
numeros.append(n1)
numeros.append(n2)
numeros.append(n3)
maior = numeros[0]
for n in numeros:
    if n > maior:
        maior = n
print("o maior numero é",maior)
