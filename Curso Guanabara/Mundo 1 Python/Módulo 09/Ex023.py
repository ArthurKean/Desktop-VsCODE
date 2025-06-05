number = input("Digite um número de até 4 digítos! ").zfill(4)
if int(number)>9999:
    print("Siga as regras!!!")
else:
    unidade = number[3]
    dezena = number[2]
    centena = number[1]
    milhar = number[0]
    print(f"Unidade {unidade}")
    print(f"Dezena {dezena}")
    print(f"Centena {centena}")
    print(f"Milhar {milhar}")