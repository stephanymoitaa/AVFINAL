salario1 = float(input("digite o valor de seu salário:"))
if salario1 > 0 and salario1 <= 2000.00:
     notimposto = (salario1)
     print("não paga imposto")

elif salario1 > 2000.00 and salario1 > 3000.00:
    impost02 = (salario1*8) / 100 
    print(f"você pagará um impoto de: {impost02}")

elif salario1 > 3000.00 and salario1 <= 4500.00:
    impost03 = (salario1*20)/100
    print(f"seu imposto é de: {impost03}")

else:
    impost02 = (salario1*29)/100
    print (f"sueimpoto é de: {impost02}")



    