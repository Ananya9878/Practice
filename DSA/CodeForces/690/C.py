def num():
    l = [str(i) for i in range(1,10)]
    d={}
    while l:
        p = l.pop(0)
        c = sum(list(map(int,(list(p)))))
        if c not in d:
            d[c] = p

        for i in range(int(p[-1])+1,10):
            h = p+str(i)
            l.append(h)
    return d

d = num()
for _ in range(int(input())):
    N = int(input())
    if N in d:
        print(d[N])
    else:
        print(-1)




