# Bài 1: Giải phương trình bậc 2. Nhập 3 số a, b, c giải pt ax^2 +bx + c = 0
from math import sqrt 
a = float(input(" nhập số a :" ))
b = float(input(" nhập số b :" ))
c = float(input(" nhập số c :" ))
delta = b**2 - ( 4*a*c )
if delta < 0 :
    print (" phương trình vô nghiệm ")
elif delta == 0 :
    print (" phương trình có nghiệm kép x1 = x2 = "  , -b/(2*a))
else : 
    x1 = (-b + sqrt(delta))/(2*a) 
    x2 = (-b - sqrt(delta))/(2*a) 
    print ("print phương trình có 2 nghiệm phân biệt " , x1 , x2  )

    
    
    






# Bài 2: phân loại tam giác
# Nhập vào 3 số a, b, c nguyên dương. kiểm tra xem a,b,c có hải là 3 cạnh của tam giác không? Nếu là ba cạnh của tam giác thì hãy phân loại xem tác giác đó thuộc loại nào
# 1. tam giác đều ||  2. tam giác vuông || 3. tam giác thường
# a = int(input("mời nhập cạnh a : "))
# b = int(input("mời nhập cạnh b : "))
# c = int(input("mời nhập cạnh c : "))
# if (a + b > c ) and (b + c > a) and (a + c > b ) :
#     print("tam giác thường ")
# elif ( a == b == c) :
#     print("tam giác đều" )
# else :
#     print("tam giác vuông")












# Bài 3: Xếp loại học sinh
# cho điểm thi Toán, Lý, Hóa, Sinh, Tin của học sinh. Hãy xếp loại kết quả của học sinh theo tiêu chí:
# 9 <= ĐTB ( điểm trung bình ) thì xếp loại xuất sắc
# 8 <= ĐTB < 9 ( điểm trung bình ) thì xếp loại giỏi
# 7 <= ĐTB < 8 ( điểm trung bình ) thì xếp loại khá
# 5 <= ĐTB < 7 ( điểm trung bình ) thì xếp loại trung bình
# 5 < ĐTB( điểm trung bình ) thì xếp loại yếu

# T = float(input("mời nhập điểm Toán :"))
# L = float(input(" mời nhập điểm Lý :"))
# H = float(input(" mời nhập điểm Hoá :"))
# S = float(input(" mời nhập điểm Sinh :"))
# Tin = float(input(" mời nhập điểm Tin :"))
# ĐTB = (T + L + H + S + Tin)/5
# print ("ĐTB là : " , ĐTB)
# if ĐTB >= 9 :
#     print("xếp loại xuất sắc ")
# elif ĐTB >= 8 and ĐTB < 9 :
#     print (" xếp loại giỏi ")
# elif ĐTB >= 7 and ĐTB < 8 :
#     print(" xếp loại khá ")
# elif ĐTB >= 5 and ĐTB < 7 :
#     print (" xếp loại trung bình")
# else :
#     print (" xếp loại yếu")
    
    
    


