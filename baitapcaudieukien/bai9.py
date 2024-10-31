# 9. Tính cước tacxi: 
# Viết chương trình tính cước taxi theo biểu phí cơ bản như sau:
# -	Loại xe 4 chỗ
#   Giá mở cửa			11.000 đồng/0.8km
#   Trong phạm vi 20km 	12.100đ/km
#   Từ km thứ 21 trở đi 		10.000 đồng/km
# -	Loại  xe 7 chỗ
#   Giá mở cửa			13.000 đồng/0.8km
#   Trong phạm vi 30km 	14.100đ/km
#   Từ km thứ 31 trở đi 		12.000 đồng/km
# Tiền chờ: 05 phút đầu được miễn phí, từ phút thứ sáu trở đi là 800đ/phút.
# Loại xe chỉ nhập 4 hoặc 7.
# Nhập thông tin từ người dùng
# Nhập thông tin từ người dùng
loai_xe = int(input("Nhập loại xe (4 hoặc 7): "))
quang_duong = float(input("Nhập quãng đường (km): "))
thoi_gian_cho = int(input("Nhập thời gian chờ (phút): "))

if loai_xe == 4:
    if quang_duong <= 0.8:
        cuoc_phi = 11000  
    else:
        cuoc_phi = 11000  
        if quang_duong <= 20:
            cuoc_phi += 12100 * (quang_duong - 0.8)  
        else:
            cuoc_phi += 12100 * (20 - 0.8)
            cuoc_phi += 10000 * (quang_duong - 20) 

elif loai_xe == 7:
    if quang_duong <= 0.8:
        cuoc_phi = 13000  
    else:
        cuoc_phi = 13000  
        if quang_duong <= 30:
            cuoc_phi += 14100 * (quang_duong - 0.8)  
        else:
            cuoc_phi += 14100 * (30 - 0.8)  
            cuoc_phi += 12000 * (quang_duong - 30)  

else:
    print("Loại xe không hợp lệ. Chỉ nhập 4 hoặc 7.")
    exit()

if thoi_gian_cho > 5:
    cuoc_phi += (thoi_gian_cho - 5) * 800  

print(f"Cước taxi: {cuoc_phi:.0f} đồng")

