a, b, c = map(int, input("Digite o comprimento de quaisquer 3 retas! ").split())
if a+b>c and a+c>b and b+c>a:
    print("Sim, estas retas podem formar um triângulo!")
else:
    print("Essas retas não formam um triângulo!")