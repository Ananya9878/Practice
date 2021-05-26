for _ in range(int(input())):
    a,b = map(int,input().split())
    res = 0
    if a == b:
        res = 0

    if a>b:
        p = abs(a-b)
        if p&1:
            res = 2
        else:
            res = 1

    if a<b:
        p = abs(a-b)
        if p&1:
            res = 1
        else:
            res = 2
    print(res)
