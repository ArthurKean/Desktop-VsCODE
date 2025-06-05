#Palindromo - Dificil
palavra = str(input("Digite uma frase!\n").strip().lower())
if palavra == palavra[::-1]:
    print(f"A frase e/ou plavra {palavra} é um palindromo")
else:
    print("Não é um palindromo")
