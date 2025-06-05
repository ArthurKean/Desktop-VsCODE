# contador = 0
# positivo = 0
# for i in range(6):
#     i = float(input())
#     if i >0:
#         contador+= 1
#         positivo+= i
# media = positivo/contador
# print(f"{contador} valores positivos")
# print(f"{media:.1f}")
    
# impares = 0
# entrada = int(input())
# if entrada%2==0:
#         valor = entrada + 1
#         impares+=1
#         print(valor)
#         valor = entrada + 3
#         impares+=1
#         print(valor)
#         valor = entrada + 5
#         impares+=1
#         print(valor)
#         valor = entrada + 7
#         impares+=1
#         print(valor)
#         valor = entrada + 9
#         impares+=1
#         print(valor)
#         valor = entrada + 11
#         impares+=1
#         print(valor)       
# else:
#     valor = entrada + 2
#     impares+=1
#     print(valor)
#     valor = entrada + 4
#     impares+=1
#     print(valor)
#     valor = entrada + 6
#     impares+=1
#     print(valor)
#     valor = entrada + 8
#     impares+=1
#     print(valor)
#     valor = entrada + 10
#     impares+=1
#     print(valor)
#     valor = entrada + 12
#     impares+=1
#     print(valor)


entrada = int(input())
impares = 0

entrada += 1

while impares < 6:
    if entrada % 2 != 0:
        print(entrada)
        impares += 1
    entrada += 1
      
