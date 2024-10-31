#3.Viết chương trình tìm số lớn nhất trong 3 số bằng Python
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
c = float(input("Nhập số thứ ba: "))

if a >= b and a >= c:
    max_num = a
elif b >= a and b >= c:
    max_num = b
else:
    max_num = c

print(f"Số lớn nhất trong 3 số là: {max_num}")
