import math

def tinh_bieu_thuc(x):
    tu_so = -x + math.sqrt(x**2 + 4)
    mau_so = math.sqrt(7 * x**4 + 1)
    if mau_so == 0:
        return "Không thể tính toán (mẫu số bằng 0)"
    return tu_so / mau_so

x = float(input("Nhập giá trị x: "))
kq = tinh_bieu_thuc(x)
print(f"Kết quả của biểu thức là: {kq}")
