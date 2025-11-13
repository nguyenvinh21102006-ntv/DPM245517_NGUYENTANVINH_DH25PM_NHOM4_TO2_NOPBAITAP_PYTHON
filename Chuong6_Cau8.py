# Nhập số lượng phần tử
n = int(input("Nhập số lượng phần tử n: "))

# Khởi tạo dãy rỗng
M = []

# Nhập từng phần tử
for i in range(n):
    while True:
        try:
            so = float(input(f"Nhập M[{i}]: "))
            M.append(so)
            break
        except ValueError:
            print("Giá trị không hợp lệ, vui lòng nhập số thực.")

# Sắp xếp dãy giảm dần
M.sort(reverse=True)

# Xuất dãy sau khi sắp xếp
print("Dãy số sau khi sắp xếp giảm dần:", M)
