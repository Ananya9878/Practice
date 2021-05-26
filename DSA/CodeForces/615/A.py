for _ in range(int(input())):
    a,b,c,n = map(int,input().split())
    p = (a+b+c+n)/3
    if p == int(p) and p>=a and p>=b and p>=c:
        print('YES')
    else:
        print('NO')