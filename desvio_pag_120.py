age = int(input("digite sua idade: "))
if age < 4:
    print("entrada gratuita")
elif age >= 4 and age < 18:
    print("ingresso R$ 5,00")
elif age >= 18 and age < 65:
    print("ingresso R$ 10,00")
else:
    print("ingresso R$ 5,00")            