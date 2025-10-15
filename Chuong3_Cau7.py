import datetime

def ngay_ke_tiep():
    try:
       
        ngay = int(input("Nhập ngày: "))
        thang = int(input("Nhập tháng: "))
        nam = int(input("Nhập năm: "))
        ngay_hien_tai = datetime.date(nam, thang, ngay)
        ngay_sau = ngay_hien_tai + datetime.timedelta(days=1)
        print("Ngày kế tiếp là:", ngay_sau.strftime("%d/%m/%Y"))

    except :
        print("Ngày không hợp lệ. Vui lòng nhập lại.")
ngay_ke_tiep()