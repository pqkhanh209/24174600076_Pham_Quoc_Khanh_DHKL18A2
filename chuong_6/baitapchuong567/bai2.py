#bài 2
x = float(input("Nhập giá trị của x: "))
if (x**4 + 1) == 0:
    print("mẫu số phải khác 0. Hãy nhập giá trị khác!")
else:
    f_x = (-x + (x**2 + 4)**(1/2)) / ((x**4 + 1)**(1/7))
    print(f"Giá trị của f(x) = {f_x:.2f}")