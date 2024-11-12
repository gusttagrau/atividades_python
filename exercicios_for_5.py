bs = int(input("digite um valor para a base "))
ex = int(input("digite um valor para expoente "))

n = bs
for i in range(0,ex-1):
    n = n * bs

print("o resultado da potencia é "+str(n))    