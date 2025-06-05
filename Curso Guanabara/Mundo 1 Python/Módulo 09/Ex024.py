city = input("Digite o nome da sua cidade natal!\n")
city1 = city.upper()
city2 = city1.split()
if city2[0] == "SANTO":
    print(f"A sua cidade natal é {city}, e ela começa com SANTO")
else:
    print(f"Sua cidade natal é {city}, porém ela não começa com SANTO")