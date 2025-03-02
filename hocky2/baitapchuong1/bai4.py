import math

def tinh_van_toc_roi_tu_do(h):
    g = 9.8
    v = math.sqrt(2 * g * h)
    return round(v, 2)

h = float(input("Nhập độ cao h (m): "))
if h < 0:
    print("Độ cao không hợp lệ. Vui lòng nhập giá trị lớn hơn hoặc bằng 0.")
else:
    v = tinh_van_toc_roi_tu_do(h)
    print(f"Vận tốc khi chạm đất: {v} m/s")
