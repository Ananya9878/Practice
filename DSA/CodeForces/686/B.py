for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    d = {}
    for i in l:
        if i not in d:
            d[i] = 1
        else:
            d[i]+=1

    if n == len(set(l)):
        m = min(l)
        p = l.index(m)
        print(p+1)
    else:
        dm = 1000000
        for i in d:
            if d[i] == 1:
                if i<dm:
                    dm = i



        if dm == 1000000:
            print(-1)
        else:
            print(l.index(dm)+1)





