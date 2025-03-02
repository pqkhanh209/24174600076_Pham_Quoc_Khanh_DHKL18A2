import math

def tinh_gia_tri_bieu_thuc(x, y):
    if (2*x + y) == 0 or (x - y) == 0 or math.cos(x) == 0:
        return "Biểu thức không xác định do mẫu số bằng 0."
    numerator = math.sin(x) / (2*x + y)
    denominator = math.cos(x) - (x**y / (x - y))
    return round(numerator / denominator, 2)

x = float(input("Nhập giá trị x: "))
y = float(input("Nhập giá trị y: "))
kq = tinh_gia_tri_bieu_thuc(x, y)
print(f"Giá trị của biểu thức: {kq}")
