n,m = map(int,input().split())
l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
l = [0]*m
for i in range(m):
    if len(l2)>0:
        a = l2.pop(0)
        p = l1.index(a)
        l1.pop(p)
        l1.insert(0,a)
        l[i] = p+1
print(*l)



