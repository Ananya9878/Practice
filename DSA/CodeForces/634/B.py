for _ in range(int(input())):
    n,a,b = map(int,input().split())
    p = 'abcdefghijklmnopqrstuvwxyz'
    s = ''
    while len(s)<n:
        s+=p[:b]
    print(s[:n])

