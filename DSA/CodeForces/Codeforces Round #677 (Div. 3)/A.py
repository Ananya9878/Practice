for _ in range(int(input())):
    n = int(input())
    a = list(str(n))
    p = a[0]
    p1 = len(a)
    res = 10*(int(p)-1)
    if len(a) == 1:
        res+=1
    elif len(a) == 2:
        res+=3
    elif len(a) == 3:
        res+=6
    elif len(a) == 4:
        res+=10
    print(res)


