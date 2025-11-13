import math

# Nhập giá trị a và x
a = float(input("Nhập cơ số a: "))
x = float(input("Nhập số x: "))

# Kiểm tra điều kiện hợp lệ
if a > 0 and a != 1 and x > 0:
    loga_x = math.log(x) / math.log(a)   # loga(x) = ln(x)/ln(a)
    print("Giá trị log_a(x) =", loga_x)
else:
    print("Lỗi: cần có a > 0, a ≠ 1 và x > 0")
