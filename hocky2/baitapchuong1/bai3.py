import math

def giai_phuong_trinh_bac_hai(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Phương trình vô nghiệm"
    elif delta == 0:
        x = -b / (2*a)
        return f"Phương trình có nghiệm kép: x = {round(x, 2)}"
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f"Phương trình có hai nghiệm: x1 = {round(x1, 2)}, x2 = {round(x2, 2)}"

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

if a == 0:
    print("Đây không phải là phương trình bậc hai.")
else:
    print(giai_phuong_trinh_bac_hai(a, b, c))