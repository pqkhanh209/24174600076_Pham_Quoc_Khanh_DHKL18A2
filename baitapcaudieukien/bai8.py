# 8. Viết chương trình phân loại sinh viên dựa vào kết quả điểm học tập. 
# Nếu điểm A thì phân loại là sinh viên xuất sắc, 
# điểm B là sinh viên loại giỏi, 
# điểm C là sinh viên loại khá, 
# điểm D là sinh viên loại trung bình, 
# điểm E là sinh viên loại yếu, 
# điểm F là sinh viên xếp loại kém.
print("Nhập điểm của sinh viên (A, B, C, D, E, F): ")

if input() == 'A':
    print("Sinh viên xuất sắc.")
elif input() == 'B':
    print("Sinh viên loại giỏi.")
elif input() == 'C':
    print("Sinh viên loại khá.")
elif input() == 'D':
    print("Sinh viên loại trung bình.")
elif input() == 'E':
    print("Sinh viên loại yếu.")
elif input() == 'F':
    print("Sinh viên xếp loại kém.")
else:
    print("Điểm không hợp lệ. Vui lòng nhập lại .")
