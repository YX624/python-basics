#角古猜想-------------------------------------
n=int(input())
if n==1:
    print("End")
else:
    while 1:
        if n%2!=0 and n!=1:
            t=n*3+1
            print(f"{n}*3+1={t}")
        elif n%2==0:
            t=n//2
            print(f"{n}/2={t}")
        elif n==1:
            print("End")
            break
        n=t

#求出e的值
n=int(input())
s=1.0
m=1
for i in range(1,n+1):
    m*=i
    t=1/m
    s=s+t
print(f"{s:.10f}")

#AQ: 数字统计--------------------------------------
a,b=map(int, input().split())
w=[]
for i in range(a,b+1):
    w.append(i)
count=0
for k in w:
    t=str(k).count('2')
    count+=t
print(count)

#AR: 计算多项式的值-------------------------------
x,n=map(float,input().split())
n=int(n)
s=0.0
for i in range(n+1):
    t=pow(x,i)
    s+=t
print(f"{s:.2f}")

#AS: 第n小的质数------------------------------------
import math
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.isqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

n=int(input())
primes=[]
t=2
while len(primes) < n:
        if is_prime(t):
            primes.append(t)
        t+=1

print(primes[-1])

#AU: 计算分数加减表达式的值
n=int(input())
t=0
s=0.0
for i in range(n):
    char=pow(-1,i)
    t=char*(i+1)
    s+=1/t
print(f"{s:.4f}")

#AW: 求阶乘的和-----------------------------------
n=int(input())
s=0
t=1
for i in range(1,n+1):
    t*=i
    s+=t
print(s)

#AX: 画矩形-----------------------------------
parts = input().split()
h = int(parts[0])
w = int(parts[1])
char = parts[2]
mode = int(parts[3])

for i in range(h):
    if mode == 1:
        print(char * w)
    else:
        if i == 0 or i == h - 1:
            print(char * w)
        else:
            print(char + ' ' * (w - 2) + char)




















































