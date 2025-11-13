import math

xA = float(input("Nhập hoành độ xA: "))
yA = float(input("Nhập tung độ yA: "))

xB = float(input("Nhập hoành độ xB: "))
yB = float(input("Nhập tung độ yB: "))
# AB = sqrt((xB - xA)^2 + (yB - yA)^2)
AB = math.sqrt((xB - xA)**2 + (yB - yA)**2)

print("Độ dài đoạn AB =", AB)
