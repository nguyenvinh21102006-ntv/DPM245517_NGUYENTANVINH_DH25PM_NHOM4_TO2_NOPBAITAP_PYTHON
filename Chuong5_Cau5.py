# Nhập chuỗi từ bàn phím
s = input("Nhập chuỗi: ")

# Khởi tạo biến đếm
hoa = thuong = so = ktdb = khoang_trang = nguyen_am = phu_am = 0

# Tập hợp nguyên âm tiếng Anh (bao gồm chữ hoa và chữ thường)
nguyen_am_set = "aeiouAEIOU"

# Duyệt từng ký tự trong chuỗi
for ch in s:
    if ch.isupper():
        hoa += 1
    elif ch.islower():
        thuong += 1
    elif ch.isdigit():
        so += 1
    elif ch.isspace():
        khoang_trang += 1
    else:
        ktdb += 1   # ký tự đặc biệt
    
    # Đếm nguyên âm / phụ âm
    if ch.isalpha():  # nếu là chữ cái
        if ch in nguyen_am_set:
            nguyen_am += 1
        else:
            phu_am += 1

# Xuất kết quả
print("Số chữ IN HOA:", hoa)
print("Số chữ in thường:", thuong)
print("Số chữ là chữ số:", so)
print("Số ký tự đặc biệt:", ktdb)
print("Số ký tự khoảng trắng:", khoang_trang)
print("Số chữ là nguyên âm:", nguyen_am)
print("Số chữ là phụ âm:", phu_am)
