n,m = map(int,input().split())
l=[]
for i in range(n):
    l.append(input())
print(l)
l1=[]
for i in range(1,n+1):
    for j in range(i+1,n+1):
        c=0
        x,y = l[i-1],l[j-1]
        for p in range(m):
            if x[p] == '1' or y[p] == '1':
                c+=1
        l1.append(c)
print(max(l1))
x = l1.count(max(l1))
print(x)

