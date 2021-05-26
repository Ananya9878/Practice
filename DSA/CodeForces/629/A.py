for _ in range(int(input())):
    a,b = map(int,input().split())
    if a%b == 0:
        print(0)
    else:
        p = int(a//b)
        p1 = b*(p+1)
        n = p1-a
        print(n)

