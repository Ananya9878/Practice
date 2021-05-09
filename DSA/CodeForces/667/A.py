for _ in range(int(input())):
    a,b = map(int,input().split())
    c = abs(a-b)
    r = c//10
    q = c%10
    if q == 0:
        res = r
    else:
        res = r+1
    print(res)
