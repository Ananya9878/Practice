n,m,d = map(int,input().split())
l = list(map(int,input().split()))
res = [0]*n
k = n-1
for i in range(m-1,-1,-1):
    for j in range(l[i]):
        res[k] = i+1
        k-=1
p = -1
while 1:
    p+=d
    if res[p] == 0:
        pass

print(res)

