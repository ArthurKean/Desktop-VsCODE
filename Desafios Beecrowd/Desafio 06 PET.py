# nota_1, nota_2 = map(float, input().split())
# if nota_1 >= 0 and nota_1 <= 10:
#     if nota_2 >= 0 and nota_2 <=10:
#         media = (nota_1 + nota_2)/2
#         print(f"media = {media:.2f}")
# else:
#         print("nota invalida")

contador = 0
soma = 0

while contador < 2:
    nota = float(input())
    if 0 <= nota <= 10:
        soma += nota
        contador += 1
    else:
        print("nota invalida")

media = soma / 2
print(f"media = {media:.2f}")
