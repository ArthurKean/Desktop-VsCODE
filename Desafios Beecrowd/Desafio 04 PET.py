M = int(input())
F1 = int(input())
F2 = int(input())
S1 = F1 + F2
F3 = M - S1
if F3>F2 and F3>F1:
    V = F3
elif F2>F1 and F2>F3:
    V = F2
else:
    V = F1
print(V)

