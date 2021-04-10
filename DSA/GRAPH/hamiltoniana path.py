def bfs(d,start,v):
    s = [[start]]
    visited = set()
    while s:
        l = s.pop(0)
        p = l[-1]
        if len(l) == v:
            if start in d[l[-1]]:
                print(l)

        if p in d:
            for i in d[p]:
                if i not in l:
                    s.append(l+[i])

def create():
    e,n = map(int,input().split())
    d = {}
    for i in range(n):
        u,v = map(int,input().split())
        if u not in d:
            d[u] = [v]
        else:
            d[u].append(v)
        if v not in d:
            d[v] = [u]
        else:
            d[v].append(u)
    bfs(d,1,e)
create()


