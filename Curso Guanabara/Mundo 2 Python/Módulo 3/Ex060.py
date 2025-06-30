print("----------------------Calculadora de Fatoriais!---------------------------------")
num = int(input("Digite um número! \n"))
list = []
list.append(num)
fatorial = 1
fatorial = fatorial * num
while num > 1:
    num = num - 1
    fatorial = fatorial * num
    list.append(num)
for c in list:
    print(f"{c} x ", end = '')

print(f"{list} = {fatorial}")
    