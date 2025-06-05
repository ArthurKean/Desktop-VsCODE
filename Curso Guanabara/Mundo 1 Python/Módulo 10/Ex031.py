km = float(input("Quantos kilometros de distância tem a sua rota? "))
if km <= 200:
    valor = 0.50*km
    print(f"Nessa viagem de {km:.0f}Km você devera pagar {valor} !")
else:
    valor = 0.45*km
    print(f"Nessa viagem de {km:.0f}Km você devera pagar {valor} !")
