numeros = []
for x in range(0,5):
    n = int(input("informe o valor: "))
    numeros.append(n)

m = numeros[0]
for x in numeros:
    if x > m:
        m = x
print("o maior valor é "+str(m))
