def create(l, v, e):
    d = {}
    for i in range(e):
        a, b, c = l[i]
        if a not in d:
            d[a] = [(b, c)]
        else:
            d[a].append((b, c))

        if b not in d:
            d[b] = [(a, c)]
        else:
            d[b].append((a, c))

    return d

def prim(g,s):
    st = [(0,s)]
    import heapq
    heapq.heapify(st)
    visited = set()
    res = 0
    while len(st)>0:
        p = heapq.heappop(st)
        if p[1] in visited:
            continue
        res+=p[0]
        visited.add(p[1])
        for i in g[p[1]]:
            heapq.heappush(st,(i[1],i[0]))

    return res

def dfs_check(g,s,e):
    st = [s]
    visited = set()
    while len(st)>0:
        p = st.pop()
        if p == e:
            return False
        if p in visited:
            continue
        visited.add(p)
        for i in g[p]:
            st.append(i[0])

    return True



def kruskal(l):
    l1 = [(i[2],i[0],i[1]) for i in l]
    l1.sort()
    d = {}
    res = 0
    for i in l1:
        c,a,b = i
        if a in d and b in d:
            if dfs_check(d,a,b):
                d[a].append((b, c))
                d[b].append((a, c))
                res+=c
        else:
            if a not in d:
                d[a] = [(b, c)]
            else:
                d[a].append((b, c))

            if b not in d:
                d[b] = [(a, c)]
            else:
                d[b].append((a, c))
            res+=c
    return res










l = [(0,1,4),(0,7,8),(1,2,8),(1,7,11),(7,8,7),(7,6,1),
     (2,8,2),(8,6,6),(6,5,2),(2,5,4),(2,3,7),
     (2,3,14),(3,4,9),(4,5,10)]


v,e = 9,14
g = create(l,v,e)
print(prim(g,0))
print(kruskal(l))