import math
ângulo_delta = float(input("Digite um ângulo qualquer!\n"))
ângulo_delta_rad = math.radians(ângulo_delta)
sen_delta = math.sin(ângulo_delta_rad)
cos_delta = math.cos(ângulo_delta_rad)
tg_delta = math.tan(ângulo_delta_rad)
print(f'O ângulo {ângulo_delta} possui o valor do seno ={sen_delta} ; coseno = {cos_delta} ; e tangente{tg_delta}')
# import sympy 
# angulox = float(input("Digite um ângulo qualquer!\n"))
# anguloxrad = sympy.rad(angulox)
# seno = sympy.sin(anguloxrad)
# cos = sympy.cos(anguloxrad)
# tan = sympy.tan(anguloxrad)
# print(f"Os valores do sen,cos e tg do ângulo {angulox} são:\n {seno} \n {cos} \n {tan} ")