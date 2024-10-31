# 4. Viết chương trình nhập vào các số a, b, c, sau đó kiểm tra bộ ba số a, b, c vừa nhập vào 
# là bộ ba cạnh của tam giác thường, tam giác vuông, tam giác cân, tam giác vuông cân, tam giác đều 
# hay không phải là bộ ba cạnh của tam giác.
a = float(input("Nhập vào cạnh a: "))
b = float(input("Nhập vào cạnh b: "))
c = float(input("Nhập vào cạnh c: "))

if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print("Đây là tam giác đều.")
    elif a == b or b == c or a == c:
        print("Đây là tam giác cân.")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Đây là tam giác vuông.")
    else:
        print("Đây là tam giác thường.")
else:
    print("Không phải là bộ ba cạnh của tam giác.")
