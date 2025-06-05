import time
velocidade = (input("Qual era a velocidade do carro em km/h?\n"))
print("PROCESSANDO......")
time.sleep(3)
if float(velocidade) > 80:
    print("Você excedeu o limite de velocidade, será multado! ")
    x1 = float(velocidade) - 80
    calculo = x1*7
    print(f"O valor da multa é R${calculo}, pois é cobrado R$7,00 por cada KM/H excedido")
else:
    print("Tudo certo")