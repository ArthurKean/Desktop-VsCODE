salário = float(input("Qual seu salário?\n"))
if salário >=0 and salário <=400.00 :
    calculo_1 = salário*15/100
    resultado_1 = salário+calculo_1
    print(f"Novo salario: {resultado_1:.2f}\nReajuste ganho: {calculo_1:.2f}\nEm percentual: 15 %")
elif salário >=400.01 and salário <=800.00 :
    calculo_2 = salário*12/100
    resultado_2 = salário+calculo_2
    print(f"Novo salario: {resultado_2:.2f}\nReajuste ganho: {calculo_2:.2f}\nEm percentual: 12 %")
elif salário >=800.01 and salário <=1200.00 :
    calculo_3 = salário*10/100
    resultado_3 = salário+calculo_3
    print(f"Novo salario: {resultado_3:.2f}\nReajuste ganho: {calculo_3:.2f}\nEm percentual: 10 %")
elif salário >=1200.01 and salário <=2000.00 :
    calculo_4 = salário*7/100
    resultado_4 = salário+calculo_4
    print(f"Novo salario: {resultado_4:.2f}\nReajuste ganho: {calculo_4:.2f}\nEm percentual: 7 %")
elif salário >2000.00 :
    calculo_5 = salário*4/100
    resultado_5 = salário+calculo_5
    print(f"Novo salario: {resultado_5:.2f}\nReajuste ganho: {calculo_5:.2f}\nEm percentual: 4 %")

    