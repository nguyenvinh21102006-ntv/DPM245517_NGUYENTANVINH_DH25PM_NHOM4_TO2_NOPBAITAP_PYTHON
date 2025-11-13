import random

N = int(input("Nhập số lượng phần tử N: "))

min_val = int(input("Nhập giá trị nhỏ nhất: "))
max_val = int(input("Nhập giá trị lớn nhất: "))
if max_val - min_val + 1 < N:
    print("Khoảng giá trị quá nhỏ để tạo N số khác nhau!")
else:
    lst = random.sample(range(min_val, max_val + 1), N)
    print("Danh sách ngẫu nhiên không trùng nhau:", lst)