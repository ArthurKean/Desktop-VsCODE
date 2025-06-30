nums1, nums2 = map (int, input("Digite 2 números separados!\n").split())
contador = 0
while contador <= 0:
    escolhido = input("Escolha um das funções! \n [1]Somar \n [2]Subtrair \n [3]Qual é o maior? \n [4]Digitar novos números \n [5]Sair do programa \n ---------->")
    if escolhido == "1":
        print(f"Função escolhida = {escolhido} \n {nums1} + {nums2} = {nums1+nums2}")
    elif escolhido == "2":
        print(f"Função escolhida = {escolhido} \n {nums1} - {nums2} = {nums1-nums2}")
    elif escolhido == "3":
        if nums1 >= nums2:
            maior = nums1
        else:
            maior = nums2
        print(f"Função escolhida = {escolhido} \n O maior é {maior}")
    elif escolhido == "4":
          print(f"Função escolhida = {escolhido} \n Escolha novos números abaixo:")
          nums1, nums2 = map(int, input("Digite 2 novos valores:").split())
    elif escolhido == "5":
        print(f"Função escolhida = {escolhido} \n Saindo do programa....")
        break
