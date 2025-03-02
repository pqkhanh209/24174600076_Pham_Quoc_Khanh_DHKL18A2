import math

def tinh_gia_tri_bieu_thuc(x):
    if x <= 0 or x == 1:
        return "Giá trị x không hợp lệ (x phải lớn hơn 0 và khác 1)."
    log4_x = math.log(x, 4)
    logx_2 = math.log(2, x)
    return round(log4_x + logx_2, 2)

x = float(input("Nhập giá trị x: "))
kq = tinh_gia_tri_bieu_thuc(x)
print(f"Giá trị của biểu thức: {kq}")