import math
n=int(input())
l=[]
c=0
for i in range(n):
    l.append(list(map(str,input().split())))
for j in range(n-1):
    for k in range(n-1):
        if l[j][k] == 'D':
            c+=1
print(math.floor(math.sqrt(c)))