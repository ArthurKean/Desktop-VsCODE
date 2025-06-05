N1, N2, N3, N4 = map(float, input().split())
media = ((N1*2)+(N2*3)+(N3*4)+(N4*1))/10
if media >= 7:
    print(f"Media: {media:.1f}")
    print("Aluno aprovado.")
elif media >= 5 and media < 7:
    print(f"Media: {media:.1f}")
    print("Aluno em exame.")
    NE = float(input())
    print(f"Nota do exame: {NE:.1f}")
    New = (media+NE)/2
    if New >=5:
        print("Aluno aprovado.")
        print(f"Media final: {New:.1f}")
    else: 
        print("Aluno reprovado.")
        print(f"Media final: {New:.1f}")
else:
    print(f"Media : {media:.1f}")
    print("Aluno reprovado.")
        