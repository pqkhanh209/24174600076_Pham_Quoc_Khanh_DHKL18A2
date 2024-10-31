# 2. Viết chương trình kiểm tra xem điểm M(x,y) có nằm trong hình tròn tâm I(a,b) và bán kính 
# R bằng cách xuất ra giá trị True nếu điểm M nằm trong hoặc trên hình tròn và False nếu nằm ngoài hình tròn, 
# với x, y, a, b, R nhập vào từ bàn phím?

x = float(input("Nhập tọa độ x của điểm M: "))
y = float(input("Nhập tọa độ y của điểm M: "))
a = float(input("Nhập tọa độ x của tâm I: "))
b = float(input("Nhập tọa độ y của tâm I: "))
r = float(input("Nhập bán kính R: "))

import math
d_binh_phuong = math.sqrt((x-a)**2 + (y-b)**2)
r_binh_phuong = r**2
if d_binh_phuong < r_binh_phuong: print('Điểm M nằm trong đường tròn')
elif d_binh_phuong==r_binh_phuong: print('Điểm M nằm trên đường tròn')
else: print('Điểm M nằm ngoài đường tròn')

