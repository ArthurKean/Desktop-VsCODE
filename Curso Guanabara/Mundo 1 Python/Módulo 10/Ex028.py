import random
print("Seja Bem-Vindo ao Jogo da Adivinhação")
print("-----------------------------------------------------")
number = random.randint(0,5)
print(number)
number_choice = int(input("Digite um número entre 0-5 para tentar advinhar!"))
if number_choice == int(number):
    print("Parabéns, você acertou!")
else:
    print("Infelizmente, você perdeu")
print("Fim de jogo")