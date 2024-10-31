# 6. Viết chương trình thể hiện menu lựa chọn gồm các thể loại phim hiện đang có trong rạp chiếu phim ABC. 
# Yêu cầu người dùng nhập lựa chọn thể loại phim muốn xem (Phim tình cảm, Phim kinh dị, Phim hoạt hình, Phim khoa học viễn tưởng)
print("Chào mừng đến với rạp chiếu phim ABC ")
print(" Vui lòng chọn thể loại phim bạn muốn xem:" )
print(" 1. Phim tình cảm" )
print(" 2. Phim kinh dị" )
print(" 3. Phim hoạt hình" )
print(" 4. Phim khoa học viễn tưởng" )

if input("Nhập số của thể loại phim bạn muốn xem (1-4): ") == '1':
    print("Bạn đã chọn thể loại Phim tình cảm.")
elif input() == '2':
    print("Bạn đã chọn thể loại Phim kinh dị.")
elif input() == '3':
    print("Bạn đã chọn thể loại Phim hoạt hình.")
elif input() == '4':
    print("Bạn đã chọn thể loại Phim khoa học viễn tưởng.")
else:
    print("Lựa chọn không hợp lệ, hãy thử lại.")
