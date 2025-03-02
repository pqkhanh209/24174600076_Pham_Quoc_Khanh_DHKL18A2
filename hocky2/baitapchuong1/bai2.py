def chuyen_doi_nhiet_do(c):
    return c + 273.15

c = float(input("Nhập nhiệt độ (°C): "))
k = chuyen_doi_nhiet_do(c)
print(f"Nhiệt độ tương ứng theo Kelvin là: {k}K")