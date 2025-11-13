import re

def NegativeNumberInStrings(s):
    # Tìm tất cả các số âm có dạng -[0-9]+
    result = re.findall(r'-\d+', s)
    
    # Chuyển chuỗi sang số nguyên
    result = [int(num) for num in result]
    
    return result

# Ví dụ chạy thử:
chuoi = "abc-5xyz-12k9l--p"
print(NegativeNumberInStrings(chuoi))
