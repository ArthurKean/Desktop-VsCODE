import time
number = int(input("Digite um número inteiro qualquer! "))
print("PROCESSANDO........")
time.sleep(3)
if number%2 == 0:
    print(f" O número {number} é par!")
else:
    print(f"O número {number} é ímpar!")
    
