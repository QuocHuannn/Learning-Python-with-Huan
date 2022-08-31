#################################################
            #  Kiểu Dữ Liệu 
#################################################

# Câu 1: Nhập số nguyên dương a có 3 chữ số. Tính tổng các chữ số của a

a = int(input("Nhập số tự nhiên có 3 chữ số: "))

# để tính tổng các chữ số, ta sẽ tách từng chứ số của a rồi cộng lại
# chữ số hàng đơn vị sẽ bằng a%10, hai chữ số còn lại tạo thành số b = a//10
donvi = a % 10
b = a // 10
# chữ số hàng chục của a bằng b%10
hangchuc = b % 10
# chữ số hàng trăm của a bằng b//10
hangtram = b // 10

sum = donvi + hangchuc + hangtram
print("Tổng chữ số : ", sum) 



# Câu 2:Cho đường tròn có bán kính R. Tính chu vi của đường tròn đó, kết quả làm tròn đến 2 chữ số thập phân
from math import pi
r = int(input("Bán kính đường tròn là : " ))
chuvi = round(2*pi*r, 2)
print("Chu vi đường tròn là: ", chuvi)




# Câu 3: Nhập ba số nguyên dương a,b,c. Hãy tìm ước chung lớn nhất của 3 số a,b,c. ** Gợi ý: dùng hàm gcd(a,b) trong module math để tìm ước chung lớn nhất của 2 số a và b
from math import gcd
a = int(input("nhập số nguyên dương a :"))
b = int(input("nhập số nguyên dương b :"))
c = int(input("nhập số nguyên dương c :"))

# Ta đặt d = gcd(a,b) khi đó ước chung lớn nhất của 3 số a,b,c sẽ bằng gcd(d,c)
d = gcd(a,b)
print ("Ước chung lớn nhất của a, b, c là:", gcd(d,c))



# Câu 4: Nhập 2 số nguyên dương a,b. Tìm bội chung nhỏ nhất của a và b. ** Gợi ý: BCNN của (a,b) = a*b//gcd(a,b)
from math import gcd
a = int(input("nhập số nguyên dương a :"))
b = int(input("nhập số nguyên dương b :"))
x = a * b // gcd(a,b)
print("Bội chung nhỏ nhất của 2 số a và b là: ", x)