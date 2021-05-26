for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    p = [l[0]]
    res = []
    for i in range(1,n):
        if p[-1]>0 and l[i]>0:
            p.append(l[i])
        elif p[-1]<0 and l[i]<0:
            p.append(l[i])
        else:
            res.append(p)
            p = [l[i]]
    res.append(p)
    ans = 0
    for i in res:
        t = i
        ans+=max(t)
    print(ans)





