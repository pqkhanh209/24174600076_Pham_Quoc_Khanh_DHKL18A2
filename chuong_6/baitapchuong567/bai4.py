#bài 4
t = int(input("Nhập thời gian sử dụng bóng đèn (s): "))
hieu_dien_the = 220 
cuong_do_dong_dien = 2.7
if t <= 0:
    print("Thời gian sử dụng phải lớn hơn 0.Hãy thử lại!")
else:
    cong_suat =(hieu_dien_the * cuong_do_dong_dien / 1000)
    cong_suat_tieu_thu = cong_suat * t / 3600
    tien_phai_tra = cong_suat_tieu_thu * 7000 
    print(f"Tiền điện phải trả: {tien_phai_tra:.0f}")

