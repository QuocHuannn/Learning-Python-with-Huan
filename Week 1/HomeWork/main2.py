#################################################
            #  Kiểu Dữ Liệu 
#################################################

# Câu 1: Nhập số nguyên dương a có 3 chữ số. Tính tổng các chữ số của a ( ví dụ nhập a = 8 thì tổng của a là 36)






# Câu 2:Cho đường tròn có bán kính R. Tính chu vi của đường tròn đó, kết quả làm tròn đến 2 chữ số thập phân
import math 
r = int(input(" bán kính đường tròn là : " ))
print ("chuvi " , 2*r*math.pi)











# Câu 3: Nhập ba số nguyên dương a,b,c. Hãy tìm ước chung lớn nhất của 3 số a,b,c. ** Gợi ý: dùng hàm gcd(a,b) trong module math để tìm ước chung lớn nhất của 2 số a và b
a = int(input("nhập số nguyên dương a :"))
b = int(input("nhập số nguyên dương b :"))
c = int(input("nhập số nguyên dương c :"))
while a! = b = c
    if a > b , a > c :
        a = a - b -c
    else b > a , b > c :
        b = b - a -c
    elif c > a , c > b :
        c = c - a - b
 




# Câu 4: Nhập 2 số nguyên dương a,b. Tìm bội chung nhỏ nhất của a và b. ** Gợi ý: BCNN của (a,b) = a*b//gcd(a,b)