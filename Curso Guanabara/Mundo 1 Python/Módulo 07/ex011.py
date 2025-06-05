#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
print("-----------------------SEJA BEM VINDO----------------------------")
print("SISTEMA DE PAGAMENTO DA LEVCAR")
dias = int(input("Quantos dias você ficou com o carro? "))
kms = float(input("Rodou quantos quilometros no veiculo? "))
calculo_1 = dias * 60
calculo_2 = kms * 0.15
resultado = float(calculo_1) + calculo_2
print(f"Você ficou {dias} dias com o carro\nPercorreu {kms} quilometros\nValor total é {resultado}")
