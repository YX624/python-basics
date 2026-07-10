#C-------------------------------------
s=input()
title=s[0]
num=float(s[1:])
if title == "C":
    res=num*1.8+32
    print(f"F{res:.2f}")
elif title == "D":
    res=(num-32)/1.8
    print(f"C{res:.2f}")

#D-------------------------------------
num=float(input("请输入人民币的数量："))
dollar=num*0.1493
print(f"{dollar:.4f}")

#E-----------------------------------
pi=3.1415927
while True:
    try:
        r = float(input())
        V = 4 / 3 * pi * r ** 3
        print(f"{V:.3f}")
    except EOFError:
        break


#J-----------------------------
n=int(input())
if n==1:
    print("Monday")
elif n==2:
    print("Tuesday")
elif n==3:
    print("Wednesday")
elif n==4:
    print("Thursday")
elif n==5:
    print("Friday")
elif n==6:
    print("Saturday")
elif n==7:
    print("Sunday")
else:
    print("input error")

#O-------------------*--------
n=int(input())
num=n**n%100
print(num)

#P-----------------------------
year=int(input())
if year%4==0 and year%100!=0 or year%400==0:
    print("yes")
else:
    print("no")

#Q------------------------------
import math
a = float(input())
b = float(input())
angle = 60 * math.pi / 180
p1 = math.sqrt(2 * a * math.sin(angle) * math.cos(angle))
x = (-b + p1) / (2 * a)
print(x)
































