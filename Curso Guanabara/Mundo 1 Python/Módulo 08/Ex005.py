import random
nomes_apresentação = ["GRUPO 01","GRUPO 02", "GRUPO 03", "GRUPO 04", "GRUPO 05"]
lista = random.sample(nomes_apresentação, len(nomes_apresentação))
print(f"Ordem sorteada: {', '.join(lista)}")
