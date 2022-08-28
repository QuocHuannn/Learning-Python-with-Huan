# Sử dụng gán cứng để in ra màn hình
# print("*\n**\n***\n****\n*****")
 
# sử dụng bằng cách gán biến phụ
# x = " Chao ban "
# print(x)

# dấu phẩy
# print("Toi ten la" ,",", "Lam Trung hieu")

#Với tham số sep
# print("a","b","c", sep = ",")

# với tham số end
# print("a", end = " ")
# print("b", end = " + ")
# print("sai")
# print("dung", end = " - ")
# print("abcd")

# sử dụng input
# x = input(print("moi nhap a: "))
# print(x)

# tính tổng
# a = int(input("Nha so a: "))
# b = int(input("Nha so b: "))
# print("Tong la: ", a+b)

# gán giá trị cho biến x
# x = " Hoc Python co ban "
# print(x)
# print(" Dia chi o nho chua bien x la: ", id(x))

# x = " Hoc Python co ban "
# print(x)
# print(" Dia chi o nho chua bien x la: ", id(x))

# x = " Da thay doi gia tri "
# print("Gia tri bien x", x)
# print("Dia chi cua bien x ", id(x))

# # gán thông thường
# a = 1
# b = 1
# c = 1
# # rút gọn
# a = b = c = 1

# # gán thông thường
# a = 1
# b = 2
# c = 3
# # rút gọn
# a, b, c = 1,2,3

# # gán thông thường
# x = a 
# a = b 
# b = x 
# # rút gọn
# a,b = b,a



########################################################################

#1.	Kiểu số nguyên – int ( là số không có phần thập phân )
#VD1:
# x = 12
# y = 13
# print("Tổng của 2 số là : ", x + y)
# print("Tổng của 2 số là : ", x * y)

#VD2:
# a = 2020
# n = 50
# s = a**n
# print(a,"lũy thừa:",n,"là:\n ",s)

#VD3:
# pi = 3.14
# r = 2
# s = pi*r*r
# print("Diện tích tam giác là: ",s)

#VD4:
# a = 2e10
# b = 2e-10
# c = a*b
# print("Giá trị của a: ",a)
# print("Giá trị của b: ",b)
# print("Giá trị của c: ",c)

#VD5:
# x = 2 + 1j
# y = 3 - 2j
# print("Tổng bằng :", x+y) 
# print("Hiệu bằng :", x-y) 
# print("Tích bằng :", x*y)


#VD6:
# x = complex(1,2)
# y = complex(0,3)
# print("x = ", x)
# print("y = ", y)

#vd7:

# x = 2
# y = 2.0
# z = 2 + 1j
# print("Kiểu dữ liệu của biến x là: ",type(x))
# print("Kiểu dữ liệu của biến y là: ",type(y))
# print("Kiểu dữ liệu của biến z là: ",type(z))


#VD8:
# from random import randint, uniform
# x = randint(-10,10)
# y = uniform(-100,100)
# print("Số nguyên tạo được : ", x)
# print("Số thực tạo được : ", y)

#VD9:
# a = 1/3
# print(a == 0.3333333333333333 )
# print(a == 0.333333334 )
# print(a == 0.3333333333333333333333334 )
# print(a == 0.333333333333333335678 )

#VD10:
# a = .3
# b = .6
# c = 0.9
# print(a+b)
# print(a+b==c)

#VD11:
# a = .3
# b = .6
# c = 0.9
# print(round(a+b,2) == round(c,2))