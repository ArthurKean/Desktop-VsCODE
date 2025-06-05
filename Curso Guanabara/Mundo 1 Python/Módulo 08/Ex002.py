# import math
# print("-------------Bem Vindo!-------------------------")
# print("   Cálculadora de hipotenusas do triangulo retângulo  ")
# cateto_oposto = float(input("Digite o valor do cateto oposto!\n"))
# cateto_adjacente = float(input("Digite o valor do cateto adjacente! \n"))
# print("...............Calculando................")
# soma = cateto_oposto**2 + cateto_adjacente**2
# resultado = math.sqrt(soma)
# print(f"A hipotenusa do triângulo retângulo é {resultado:.2f}")
import math
print("-------------Bem Vindo!-------------------------")
print("   Cálculadora de hipotenusas do triangulo retângulo  ")
cateto_oposto = float(input("Digite o valor do cateto oposto!\n"))
cateto_adjacente = float(input("Digite o valor do cateto adjacente! \n"))
print("...............Calculando................")
soma = math.hypot(cateto_oposto, cateto_adjacente)
print(f"A hipotenusa do triângulo retângulo de lados {cateto_oposto} e {cateto_adjacente} é igual a {soma}")