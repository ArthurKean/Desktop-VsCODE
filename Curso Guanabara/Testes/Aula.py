# m = [[1,2,3,4], [2,3,4,5], [3,4,5,6]]
# def maiorMatrix(m):
#     maior_valor = m[0] [0]
#     for linha in m:
#         for col in linha:
#             if col > maior_valor:
#                 maior_valor = col
#     return maior_valor
# print(maiorMatrix(m))

# ---------------------------------------------

# m = [[1,2,3,4], [2,3,4,5], [3,4,5,6]]
# def Maiormatrix(m):
#     maior_valor = m[0] [0]
#     linhas = len(m)
#     colunas = len(m[0])
#     for i in range(linhas):
#         for j in range(colunas):
#             if m[i] [j] > maior_valor:
#                 maior_valor = m[i] [j]
#     return maior_valor
# print(Maiormatrix(m))

# -------------------------------------------------

# m = [[1,2,3,4], [2,3,4,5], [3,4,5,6]]
# def somatoria(m):
#     linhas = len(m)
#     colunas = len(m[0])
#     somatorio = 0
#     for i in range(linhas):
#         for j in range(colunas):
#             if m[i][j] % 2 == 1:
#                 somatorio += m[i][j]
#     return somatorio
# print(somatoria(m))

# ------------------------------------------------
# m = [[1,2,3,4], [2,3,4,5], [3,4,5,6]]
# def linhamaior(m):
#     maior_linha = sum(m[0])
#     for linha in m:
#         soma_linha = sum(linha)
#         if soma_linha > maior_linha:
#             maior_linha = soma_linha
#     return maior_linha
# print(linhamaior(m))

# ------------------------------------------------------
# def maiorsomacoluna(m):
#     maior_coluna = 


# ---------------------------------------------------------

# from math import sqrt
# a, b, c = map(float, input("Coloque 3 valores! \n").split())
# delta = pow(b,2) - 4 * a * c
# if delta < 0 or a == 0:
#     print("Impossivel calcular")
# else:
#     raiz_positiva = (-(b) + sqrt(delta))/(2 * a)
#     raiz_negativa = (-(b) - sqrt(delta))/(2 * a)
#     print(f"R1 = {raiz_positiva:.5f}")
#     print(f"R2 = {raiz_negativa:.5f}")

# -----------------------------------------------------

# n1, n2 ,n3 = map(int, input().split())
# maior= max(n1,n2,n3)
# menor= min(n1,n2,n3)
# meio = (n1+n2+n3) - maior - menor
# print(f"{menor}\n{meio}\n{maior} \n \n{n1}\n{n2}\n{n3}")