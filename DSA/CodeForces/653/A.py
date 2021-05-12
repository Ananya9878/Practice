for _ in range(int(input())):
    x,y,n = map(int,input().split())
    a = n%x
    num = n-a
    if a>=y:
        res = num + y
    else:
        res = num-(x-y)
    print(res)


