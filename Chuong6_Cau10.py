# Hàm nhập ma trận
def nhap_matrix(m, n, name=""):
    print(f"Nhập ma trận {name} ({m}x{n}):")
    mat = []
    for i in range(m):
        row = []
        for j in range(n):
            while True:
                try:
                    val = float(input(f"A[{i+1},{j+1}] = "))
                    row.append(val)
                    break
                except ValueError:
                    print("Giá trị không hợp lệ, vui lòng nhập số.")
        mat.append(row)
    return mat

# Hàm cộng 2 ma trận
def cong_matrix(A, B):
    m = len(A)
    n = len(A[0])
    C = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(A[i][j] + B[i][j])
        C.append(row)
    return C

# Hàm tính ma trận chuyển vị
def chuyen_vi(matrix):
    m = len(matrix)
    n = len(matrix[0])
    transposed = []
    for j in range(n):
        row = []
        for i in range(m):
            row.append(matrix[i][j])
        transposed.append(row)
    return transposed

# Hàm xuất ma trận
def in_matrix(matrix, name="Matrix"):
    print(f"{name}:")
    for row in matrix:
        print(row)
    print()

# Nhập kích thước ma trận
m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))

# Nhập ma trận A và B
A = nhap_matrix(m, n, "A")
B = nhap_matrix(m, n, "B")

# Cộng 2 ma trận
C = cong_matrix(A, B)

# Tính ma trận chuyển vị
A_T = chuyen_vi(A)
B_T = chuyen_vi(B)

# Xuất kết quả
in_matrix(A, "Ma trận A")
in_matrix(B, "Ma trận B")
in_matrix(C, "Ma trận C = A + B")
in_matrix(A_T, "Ma trận A chuyển vị")
in_matrix(B_T, "Ma trận B chuyển vị")
