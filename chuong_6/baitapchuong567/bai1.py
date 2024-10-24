#bài 1
r = float(input("Nhập vào bán kính: "))
h = float(input("Nhập vào chiều cao: "))
pi = 3.14

if r <= 0 or h <= 0:
    print("r và h phải lớn hơn 0. Hãy thử lại!")
else:
    dtxq = 2 * pi * r * h
    dttp = dtxq + 2 * pi * r**2
    the_tich = pi * r**2 * h
    print(f"Diện tích xung quanh: {dtxq:.2f}")
    print(f"Diện tích toàn phần: {dttp:.2f}")
    print(f"Thể tích:{round(the_tich,2)}")