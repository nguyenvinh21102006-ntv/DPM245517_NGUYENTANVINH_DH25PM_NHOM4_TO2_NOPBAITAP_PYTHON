'''Viết chương trình nhập vào điểm ba môn Toán, Lý, Hóa của một học sinh. In ra
điểm trung bình của học sinh đó với hai số lẻ thập phân.'''

dt=float(input("Nhap diem toan: "))
dl=float(input("Nhap diem ly: "))
dh=float(input("nhap diem hoa: "))
dtb=(dt+dl+dh)/3
print("diem trung binh",dtb)
print("diem trung binh",round(dtb,2))
