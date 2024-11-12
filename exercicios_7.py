salario = float(input("digite o seu salario:"))

valor_aumento = 0
novo_salario = 0

if salario <= 280:
    valor_aumento = salario * 20 / 100
    novo salario = salario + valor_aumento
    print("O seu salario é "+str(salario)+"20% de aumento. O valor é "+str(novo_salario))

elif salario < 700:
    valor_aumento = salario * 10 / 100
    novo salario = salario + valor_aumento
    print("O seu salario é "+str(salario)+"15% de aumento. O valor é "+str(novo_salario))

elif salario < 1500:
    valor_aumento = salario * 10 / 100
    novo salario = salario + valor_aumento
    print("O seu salario é "+str(salario)+"10% de aumento. O valor é "+str(novo_salario))

else:
    valor_aumento = salario * 5 / 100
    novo salario = salario + valor_aumento
    print("O seu salario é "+str(salario)+"5% de aumento. O valor é "+str(novo_salario))