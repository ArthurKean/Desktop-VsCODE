primero_termo, razão = map(int, input("Digite o primeiro termo e a razão da P.A! \n").split())
n = 1
while n <= 10:
    an = primero_termo + (n-1)* razão
    print(f"{an}", end = " ") 
    n+=1
