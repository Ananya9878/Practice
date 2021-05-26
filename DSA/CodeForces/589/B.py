
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    c = 0
    s = sorted(l)
    h = set()
    while c!=n-1 and s:
        k = s.pop(0)
        idx = l.index(k)
        while idx>0 and c!=n-1 and idx not in h:
            if l[idx-1]>k:
                l[idx-1],l[idx] = l[idx],l[idx-1]
                c+=1
                h.add(idx)
                idx-=1
            else:
                break
   

    print(*l)






