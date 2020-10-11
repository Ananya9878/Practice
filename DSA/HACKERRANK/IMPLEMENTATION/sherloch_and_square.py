import math

for i in range(int(input())):
    c=0
    a,b = list(map(int,input().split()))
    for i in range(a,b+1):
        x=math.sqrt(i)
        if (x-(math.floor(x)))==0:
            c+=1
    print(c)

