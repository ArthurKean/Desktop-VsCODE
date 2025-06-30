gênero = str(input("Qual o seu gênero?\n"))
sexo = gênero.upper()
while sexo !="M" and sexo !="F":
    print("Digite novamente!")
    gênero = str(input("Qual o seu gênero?\n"))
    sexo = gênero.upper()
if sexo == "M":
    print("Sexo masculino")
else:
    print("Sexo feminino")
    
    