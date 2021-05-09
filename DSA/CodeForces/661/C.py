def count(l,n,k):
    res=0
    i,j = 0,n-1
    while i<j:
        if l[i]+l[j] == k:
            res+=1
            i+=1
            j-=1
        elif l[i]+l[j]<k:
            i+=1
        else:
            j-=1
    return res

for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    l.sort()
    c = 0
    for i in range(2,2*(n+1)):
        t = count(l,n,i)
        if t>c:
            c = t
    print(c)

