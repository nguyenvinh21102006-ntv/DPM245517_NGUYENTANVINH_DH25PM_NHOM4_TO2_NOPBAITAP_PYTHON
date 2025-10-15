n = int(input("Nhập kích thước hình vuông n: "))
for i in range(n):
    if i == 0 or i == n - 1:
        print('*' * n)
    else:
        print('*' + ' ' * (n - 2) + '*')

m = int(input("Nhập chiều cao m: "))
for i in range(1, m + 1):
    print(' ' * (m - i) + '*' * i)

    