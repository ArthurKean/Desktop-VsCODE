# Entrada: l1 = [2,4,3], l2 = [5,6,4]
# Saída: [7,0,8]
# Explicação: 342 + 465 = 807.
# Exemplo 2:

# Entrada: l1 = [0], l2 = [0]
# Saída: [0]
# Exemplo 3:

# Entrada: l1 = [9,9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Saída: [8,9,9,9,0,0,0,1]
def isPalindrome(self, x):
    x_str = str(x)
    x_invertido = x_str[::-1]
    if x == int(x_invertido):
        return True
    return False
print(isPalindrome(10,121))