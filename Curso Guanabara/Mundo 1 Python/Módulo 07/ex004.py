nota_1 = float(input("Nota da P1: "))
nota_2 = float(input("Nota da P2: "))
media = (nota_1 + nota_2)/2
print(f"A média desse aluno foi {media}")
if media>=7:
    print("O aluno foi aprovado")
else:
    print("O aluno foi reprovado")