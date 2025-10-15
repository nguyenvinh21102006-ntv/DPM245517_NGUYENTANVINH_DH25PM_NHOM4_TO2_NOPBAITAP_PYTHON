a=int(input("Nhập vào a:" ))
b=int(input("Nhập vào b:" ))
t=(input("Nhập vào một phép toán +,-,*,/: "))

if t=='+':
    kq=a+b
elif t=='-':
    kq=a-b
elif t=='*':
    kq=a*b
elif t=="/":
    if b != 0:
        kq=a/b
    else:
        print("phép tính bị lỗi!")
else:
    print("Phép toán không hợp lệ!")
print("Kết quả = ",kq)