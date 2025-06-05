#Caçador de primos
numero = int(input("Digite um número!\n"))
total = 0
for c in range(1,numero+1):
    if numero % c == 0:
        print(f"É divisivel por {c}")
        total += 1
    else:
        print(f"Não é divisivel por {c}")  
if total == 2:
    print(f"O numero {numero} é primo!")
else:
    print("O número não é primo")
        