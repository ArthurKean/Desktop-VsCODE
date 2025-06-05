# #Maioridade
# ano1, ano2, ano3, ano4, ano5, ano6, ano7 = map(int, input("Digite seu ano de nascimento!\n").split())
# valores = [ano1, ano2, ano3, ano4, ano5, ano6, ano7]
# maiores = 0
# menores = 0
# for c in valores:
#     if (2024 - c) >= 18:
#         # print(f"Você nasceu em {c} e já completou a maioridade")
#         maiores += 1
#     else:
#         # print(f"Você nasceu em {c} e ainda não completou a maioridade")
#         menores += 1
# print(f"Então {maiores} atingiram a maioridade e {menores} ainda irão!")
# -----------------------------------------------------
# maiores = 0
# menores = 0
# for c in range(1,8):
#     ano = int(input("Digite o ano de nascimento!\n"))
#     if (2025 - ano) >= 18:
#         maiores +=1
#     else:
#         menores +=1
# print(f"{maiores} São maiores de 18 e {menores} são menores de 18!")