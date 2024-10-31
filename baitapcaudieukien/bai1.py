# 1. Tính năm nhuận. Năm thứ n là nhuận nếu nó chia hết cho 4, nhưng không chia hết cho 100 hoặc chia hết 400. 
nam = 2024
if nam % 4 == 0:
    if nam % 100 == 0:
        if nam % 400 == 0:
            print(f"Năm {nam} là năm nhuận.")
        else:
            print(f"Năm {nam} không phải là năm nhuận.")
    else:
        print(f"Năm {nam} là năm nhuận.")
else:
    print(f"Năm {nam} không phải là năm nhuận.")