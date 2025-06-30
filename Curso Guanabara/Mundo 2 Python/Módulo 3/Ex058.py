import random
contador=1
numero_aleatorio=random.randint(0,10)
numero_escolhido = int(input("Escolha um número:\n"))

while numero_aleatorio != numero_escolhido:
    numero_escolhido = int(input("Escolha um número:\n"))
    contador +=1
    
print(f"Parabéns o número pensado foi {numero_aleatorio} e você acertou com {contador} tentativas!")


