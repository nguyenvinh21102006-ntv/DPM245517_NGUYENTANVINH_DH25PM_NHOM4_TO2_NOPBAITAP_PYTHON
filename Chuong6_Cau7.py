# Nhập số lượng phần tử
N = int(input("Nhập số lượng phần tử của dãy: "))

# Khởi tạo dãy rỗng
day_so = []

# Nhập từng phần tử
for i in range(N):
    while True:
        try:
            so = int(input(f"Nhập số thứ {i+1}: "))
            
            # Kiểm tra thứ tự tăng dần
            if i == 0 or so > day_so[-1]:
                day_so.append(so)
                break
            else:
                print(f"Số nhập phải lớn hơn {day_so[-1]}. Vui lòng nhập lại.")
        except ValueError:
            print("Giá trị không hợp lệ, vui lòng nhập số nguyên.")

# In dãy số sau khi nhập xong
print("Dãy số đã nhập:", day_so)
