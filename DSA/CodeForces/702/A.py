def check(a,b):
    c=0
    if a>b:
        while b*2<a:
            b = b*2
            c+=1
    else:
        while a*2<b:
            a = a*2
            c+=1
    return c
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    res=0
    for i in range(n-1):
        p = check(l[i],l[i+1])
        res+=p
    print(res)


