print("-------------------"*10)
print("                                                                  Portal do Alistamento")
nascimento = int(input("Qual a sua data de nascimento(apenas ano)?\n"))
idade = 2025 - nascimento
if idade < 18:
    prazo = 18 - idade
    print(f"Para você se alistar faltam {prazo} anos!")
elif idade == 18:
    print(f"Você deve se alistar imediatamente")
elif idade > 18:
    pergunta = input("Você ja se alistou?\n")
    if pergunta == "sim":
        print("Fique tranquilo")
    else:
        prazo = idade - 18
        print(f"Você tem pendências para com o exercito brasileiro, está devendo {prazo} anos!")
else:
    print("Digite um valor válido!")