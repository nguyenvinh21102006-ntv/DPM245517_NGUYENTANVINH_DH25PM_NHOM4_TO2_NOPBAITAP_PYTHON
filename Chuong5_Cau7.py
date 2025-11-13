def ToiUuChuoiDanhTu(s):
    s = s.strip()
    words = s.split()
    words = [word.capitalize() for word in words]
    return ' '.join(words)

chuoi = input("Nhập chuỗi: ")

chuoi_toi_uu = ToiUuChuoiDanhTu(chuoi)
print("Chuỗi tối ưu:", chuoi_toi_uu)
