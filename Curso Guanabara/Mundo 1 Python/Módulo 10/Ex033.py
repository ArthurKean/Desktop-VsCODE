n1, n2, n3 = map(int, input("Digite 3 números inteiros separados por espaço: ").split())
maior = max(n1, n2, n3)
menor = min(n1, n2, n3)
if n1==n2==n3:
    print("Todos são iguais!")
else:
    if maior == n1:
        print(f"O maior é o n1 = {n1}")
    elif maior == n2:
        print(f"O maior é o n2 = {n2}")
    else: 
        print(f"O maior é o n3= {n3}")
if menor == n1:
    print(f"O menor é n1= {n1}")
elif menor == n2:
    print(f"O menor é igual a n2= {n2}")
else:
    print(f"O menor é igual a n3= {n3}")

