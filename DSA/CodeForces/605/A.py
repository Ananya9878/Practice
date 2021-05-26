for _ in range(int(input())):
    a,b,c = map(int,input().split())
    l = [a,b,c]
    l.sort()
    a, b, c = l
    if abs(a-c)<=1:
        print(0)
    else:

        a = a+1
        c = c-1
        d = abs(a-c)*2
        print(d)