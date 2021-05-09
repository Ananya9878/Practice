for _ in range(int(input())):
    n,k = map(int,input().split())
    l = [i for i in range(1,n+1)]
    if k == 0:
        print(*l)
        continue
    p = [l.pop(0)]
    c=0
    i,j = 0,n
    while len(l)>=2:
        a = l.pop()
        b = l.pop(0)
        p.append(a)
        p.append(b)
        c+=1
        if c == k:
            break

    if c == k:
        d = p+l
        print(*d)
    else:
        print(-1)

    # for i in range(n):
    #     for j in range(i,n):
    #         for k in range(j,n):
    #             if l[i]>l[j] and l[i] > l[k]:
    #                 if l[i] not in p and l[j] not in

