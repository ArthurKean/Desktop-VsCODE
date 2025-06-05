print("BEM VINDO AO CALCULADOR AUTOMÁTICO DA TABUADA")
number = int(input("Digite um número entre 1 e 100: "))
#print(f"{number} x 1 = {number*1}")
#print(f"{number} x 2 = {number*2}")
print(f"\nTabuada do {number}:\n")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")