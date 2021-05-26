for _ in range(int(input())):
    n,m = map(int,input().split())
    res = 0
    if n == 1:
        res = 0
    elif n == 2:
        res = m
    else:
        res  = 2*m
    print(res)
