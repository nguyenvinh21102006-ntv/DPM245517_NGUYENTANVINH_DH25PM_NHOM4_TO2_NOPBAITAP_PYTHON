import math

# Nhập giá trị x
n = float(input("Nhập giá trị n: "))

# Tính căn bậc 2 lồng nhau
S = math.sqrt(n + math.sqrt(n + math.sqrt(n + math.sqrt(n))))

# Xuất kết quả
print("Giá trị căn bậc 2 lồng nhau là:", S)
