for _ in range(int(input())):
    n,x = map(int,input().split())
    c = 1
    l = [2]
    while l[-1]<n:
        l.append(l[-1]+x)
    print(len(l))

