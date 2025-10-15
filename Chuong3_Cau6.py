def doc_so(n):
    hang_don_vi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    hang_chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi",
                 "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]

    if n < 0 or n > 99:
        return "Số không hợp lệ. Chỉ nhập số từ 0 đến 99."
    if n < 10:
        return hang_don_vi[n] if n != 0 else "không"
    chuc = n // 10
    don_vi = n % 10
    if n == 10:
        return "mười"
    if don_vi == 1 and chuc > 1:
        return hang_chuc[chuc] + " mốt"
    elif don_vi == 5 and chuc > 0:
        return hang_chuc[chuc] + " lăm"
    elif don_vi == 0:
        return hang_chuc[chuc]
    else:
        return hang_chuc[chuc] + " " + hang_don_vi[don_vi]

n = int(input("Nhập số nguyên từ 0 đến 99: "))
print("Cách đọc:", doc_so(n))