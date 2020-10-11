from itertools import combinations
for i in range(int(input())):
    n = int(input())
    res=[0]*n
    l = list(map(int,input().split()))
    l1= []
    for j in range(1,n+1):
        l1+=list(combinations(l,j))
    # print(l1)

    for p in l1:
        if len(p) == 1:
            mini = p[0]
            res[mini-1]+=1
        elif len(set(p)) == len(p):
            mini = min(p)
            res[mini-1]+=1
        else:
            d={}
            for a in p:
                if a in d:
                    d[a]+=1
                else:
                    d[a]=1
            y = max(d.values())

            l2=[]
            for u in d.keys():
                if d[u] == y:
                    l2.append(u)
            mini = min(l2)

            res[mini-1]+=1
    print(*res)





