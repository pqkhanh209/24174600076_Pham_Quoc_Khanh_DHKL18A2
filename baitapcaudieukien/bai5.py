# 5. Viết chương trình kiểm tra một ký tự trong bảng chữ cái tiếng anh là nguyên âm hay phụ âm. 
# Ký tự là bất kỳ được nhập từ bàn phím.
ky_tu = input("Nhập một ký tự: ")

if ky_tu == 'a' or ky_tu == 'e' or ky_tu == 'i' or ky_tu == 'o' or ky_tu == 'u':
    print("Đây là nguyên âm.")
elif 'a' <= ky_tu <= 'z':  
    print("Đây là phụ âm.")
else:
    print("Ký tự không hợp lệ.")
