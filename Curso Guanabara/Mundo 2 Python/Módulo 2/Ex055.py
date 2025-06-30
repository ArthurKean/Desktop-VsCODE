#Mais gordo e menos gordo
peso1, peso2, peso3, peso4, peso5 = map(float, input("Digite o seu pesso em Kilogramas!\n").split())
valores = [peso1, peso2, peso3, peso4, peso5]
maior = max(valores)
menor = min(valores)
print(f"O maior peso foi {maior} e o menor foi {menor}")