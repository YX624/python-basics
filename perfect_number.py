n=int(input())
res=[]
for a in range(2,n+1):
    a3=a**3
    for b in range(2,n+1):
        b3=b**3
        if b3>a3:
            break
        for c in range(b,n+1):
            c3=c**3
            if b3+c3>a3:
                break
            for d in range(c,n+1):
                d3=d**3
                s=b3+c3+d3
                if s==a3:
                    res.append((a,b,c,d))

for a,b,c,d in res:
    print(f"Cube = {a},Triple = ({b},{c},{d})")
                
#题目是找出符合这个立方形式的多组数据        
            #a**3==b**3+c**3+d**3
    
