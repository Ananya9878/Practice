for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    d = {0:0,1:0,2:0}
    for i in range(len(l)):
        a = l[i]%3
        d[a]+=1

    s = n//3
    res = 0
    c0,c1,c2 = d[0],d[1],d[2]

    while c0!=c1 or c1!=c2:
        if c0>s:
            res += (c0 - s)
            c1+=(c0-s)
            c0 = s
        if c1>s:
            res += (c1 - s)
            c2 += (c1 - s)
            c1 = s

        if c2>s:
            res += (c2 - s)
            c0 += (c2 - s)
            c2 = s
    print(res)





