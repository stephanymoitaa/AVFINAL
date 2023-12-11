salarioatual = float(input("digite seu salàrio atual"))
if salarioatual > 0 and salarioatual < 400.00:
    newsalario = (salarioatual*15)/100
    nuevosalario = (newsalario+salarioatual)
    print (f"seu salário atual è de:{nuevosalario}")
    print (f"o valor do reajuste è de>:{newsalario}")
    print (f"o percentual de ajuste ~e de 15%")

if salarioatual > 400.01 and salarioatual <= 800.00:
    salario20 = (salarioatual*12)/100
    salario21 = (salarioatual+salario20)
    print (f"seu salário atual é de:{salario21}")
    print (f"o valor do reajuste é de >:{salario20}")
    print (f"o percentual de ajuste é de 12%")

if salarioatual > 800.01 and salarioatual <= 1200.00:
   salario23 = (salarioatual*11)/100
   salario25 = (salarioatual+salario20)
   print (f"seu salário atual é de:{salario20}")
   print (f"o valor do reajuste é de>:{salario21}")
   print (f"o percentual de ajuste é de 7%")

else:
    ajuste05 = (salarioatual*4)/100
    ajuste = (salarioatual+ajuste05)
    print (f"seu salàrio atual é de:{ajuste05}")
    print (f"o valor do rejuste é de:{ajuste}")
    print (f"o percentual de ajuste é de 4%")