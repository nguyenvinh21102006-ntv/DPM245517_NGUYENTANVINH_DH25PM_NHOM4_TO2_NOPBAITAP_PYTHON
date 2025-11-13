import random

check = [4.5, 34, -1, 100, 0, 99]
possible_values = range(0, 100)

for v in check:
    if v in possible_values:
        print(f"{v} có thể xuất hiện")
    else:
        print(f"{v} không thể xuất hiện")
