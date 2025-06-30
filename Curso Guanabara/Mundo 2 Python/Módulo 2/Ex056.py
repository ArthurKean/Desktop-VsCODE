#Analisador Completo
media = 0
homem_maisvelho = 0
nome_maisvelho = ''
mulheres = 0
for p in range(1,5):
    nome, idade, sexo = input("Digite seu nome, idade e sexo!\n").split()
    idade_int = int(idade)
    media += idade_int
    if sexo == "masculino":
        if idade_int > homem_maisvelho:
            homem_maisvelho = idade_int
            nome_maisvelho = nome
    if sexo == "feminino":
        if idade_int<20:
            mulheres+=1
media_geral = (media/4)
print(f"A media das idades das 4 pessoas é {media_geral}")
print(f"Existe(m) {mulheres} mulheres menores de 20 anos")
print(f"O homem mais velho é o {nome_maisvelho}, pois ele tem {homem_maisvelho} anos")


