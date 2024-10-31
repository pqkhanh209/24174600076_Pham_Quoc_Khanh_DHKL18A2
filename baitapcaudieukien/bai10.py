# 10. Viết chương trình nhập lương nhân viên, tính thuế thu nhập và lương ròng (số tiền
# lương thực sự mà nhân viên đó nhận được).
# Với các thông số giả sử như sau
# • 30% thuế thu nhập nếu lương là 15 triệu.
# • 20% thuế thu nhập nếu lương từ 7 đến 15 triệu.
# • 10% thuế thu nhập nếu lương dưới 7 triệu.
# Nhập lương của nhân viên
luong = float(input("Nhập lương của nhân viên (đồng): "))

if luong > 15000000:
    thue = 0.3 * luong  
    luong_rong = luong - thue
elif luong >= 7000000:
    thue = 0.2 * luong 
    luong_rong = luong - thue
else:
    thue = 0.1 * luong
    luong_rong = luong - thue

print(f"Thuế thu nhập: {thue:.0f} đồng")
print(f"Lương ròng: {luong_rong:.0f} đồng")