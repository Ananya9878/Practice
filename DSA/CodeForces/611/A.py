for _ in range(int(input())):
    h,m = map(int,input().split())
    c,d = 24,60
    c1 = 24-h
    res = c1*60-m
    print(res)