import math

# Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Nhập mảng số tự nhiên
n = int(input("Nhập số lượng phần tử của mảng: "))
arr = []
for i in range(n):
    while True:
        try:
            num = int(input(f"Nhập phần tử thứ {i+1}: "))
            if num < 0:
                print("Vui lòng nhập số tự nhiên (>=0).")
            else:
                arr.append(num)
                break
        except ValueError:
            print("Giá trị không hợp lệ, vui lòng nhập số nguyên.")

# Tách số lẻ, số chẵn, số nguyên tố
le = [x for x in arr if x % 2 == 1]
chan = [x for x in arr if x % 2 == 0]
nguyen_to = [x for x in arr if is_prime(x)]
khong_nguyen_to = [x for x in arr if not is_prime(x)]

# Xuất kết quả
print("Số lẻ:", le, ", Tổng số lẻ:", len(le))
print("Số chẵn:", chan, ", Tổng số chẵn:", len(chan))
print("Số nguyên tố:", nguyen_to)
print("Không phải số nguyên tố:", khong_nguyen_to)
