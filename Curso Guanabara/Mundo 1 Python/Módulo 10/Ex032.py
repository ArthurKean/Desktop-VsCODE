print("----------------------------------------------------------------------------")
print("Calculadora de ano bissexto!")
ano = int(input("Digite um ano de 4 dígitos: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"Parabéns, o ano {ano} é bissexto!")
else:
    print(f"O ano {ano} não é bissexto.")
