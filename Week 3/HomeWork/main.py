# SỬ DỤNG CẤU TRÚC LẶP
# Cho một số tự nhiên n (n <= 10^1000).
# Tính tổng các chữ số của n.
# vd: n = 123. Tổng các chữ số bằng 1 + 2 + 3 = 6
# a = int(input("nhập số a :"))
# b = int(input("nhập số b :"))
# c = int(input("nhập số c :"))
# n = 0
# for x in a , b ,c :
#     n = n + x
# print("tổng cua a + b + c là " , n )











# Cho một số tự nhiên n (n <= 10^1000).
# TÌm chữ số lớn nhất và nhỏ nhất
# VD: n = 123 . Min = 1 & Max = 3
# n = 5, 7 ,9
# print(" số lớn nhất là " , max(n))
# print (" số nhỏ nhất là " , min(n))








# Tìm ước chung lớn nhất và bội chung nhỏ nhất của 2 số a và b
# VD: a = 9 và b = 6 thì ước chung lớn nhất bằng 3, bội chung nhỏ nhất bằng 18
# a = int(input("Nhập số  a = "))
# b = int(input("Nhập số  b = "))
# def ucln(a, b):
#     if (b == 0):
#         return a;
#     return ucln(b, a % b);
# def bcnn(a, b):
#     return int((a * b) / ucln(a, b));
# print("Ước  chung lớn nhất của a và b là : " , ucln(a,b))
# print("Bội chung nhỏ nhất của a và b là : " , bcnn(a,b))









# Kiểm tra số nguyên tố, cho 1 số n < 10^9. Kiểm tra xem nó có phải là số nguyên tố k
# def kiemtra_songuyento(n):
#     count = 0
#     for i in range(1 , n + 1):
#         if n < 2:
#             print(True)
#         elif n==2:
#             print(False)    
#         elif n % 2:
#             print(False)    
#         else:
#             for i in range (3 , n , 2):
#                 if i%n == 0:
#                     print(False) 
# n = int(input("moi ban nhap 1 so bat ky: "))
# if n ==  True:
#     print("la so nguyen to")
# else:
#     print("khong phai so nguyen to")                   

     
        
    
    
