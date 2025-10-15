import math

x = float(input("Nhập giá trị x: "))
n = int(input("Nhập giá trị n: "))
S = 0
for i in range(n + 1):
    mu = 2 * i + 1
    S += x**mu / math.factorial(mu)
print(f"S({x}, {n}) =", S)