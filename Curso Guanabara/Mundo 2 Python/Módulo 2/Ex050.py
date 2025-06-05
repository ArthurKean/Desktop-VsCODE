# #Soma de apenas números pares
# n1, n2, n3, n4, n5, n6 = map(int, input("Digite 6 valores inteiros!\n").split())
# valores = [n1, n2, n3, n4, n5, n6]
# contador = 0
# for n in valores:
#     if n%2 == 0:
#         contador+= n
# print(contador)

contador = 0
soma = 0
for c in range(1,7):
    valor = int(input("Digite um valor!\n"))
    if valor%2 == 0:
        soma += valor
        contador += 1
print(f"Você colocou {contador} PARES e a soma deu {soma}")
    
