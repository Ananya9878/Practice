for _ in range(int(input())):
    n = int(input())
    l = []
    s = ''

    for i in range(n):
        a,b = map(int,input().split())
        l.append((a,b))

    l.sort()
    l = sorted(l, key = lambda x: x[1])
    p = l[0]
    s+='R'*p[0]
    s+='U'*p[1]
    for i in range(n-1):
        p,q = l[i],l[i+1]
        c,d,e,f = p[0],p[1],q[0],q[1]
        s += 'R' * (e-c)
        s += 'U' * (f-d)
    h = l[-1]
    if h[0]+h[1] == len(s):
        print('YES')
        print(s)
    else:
        print('NO')







