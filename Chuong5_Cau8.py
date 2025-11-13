import os

# Hàm lấy tên file kèm đuôi
def LayTenFile(path):
    return os.path.basename(path)

# Hàm lấy tên bài hát (bỏ phần đuôi)
def LayTenBaiHat(path):
    filename = os.path.basename(path)
    name, ext = os.path.splitext(filename)
    return name

# Nhập đường dẫn từ người dùng
duong_dan = input("Nhập đường dẫn file nhạc: ")

# Xuất kết quả
print("Tên file:", LayTenFile(duong_dan))
print("Tên bài hát:", LayTenBaiHat(duong_dan))
