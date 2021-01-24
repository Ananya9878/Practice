def create():
    graph=[]
    f = open('input.txt','r')
    v,e = map(int,f.readline().split())
    for i in range(e):
        a,b,c = map(int,f.readline().split())
        graph.append((a,b,c))

    return graph,v,e

def check(g,start,end):
    s = [start]
    visited = set()
    while len(s)>0:
        p = s.pop(0)
        if p == end:
            return True
        if p in visited:
            continue
        visited.add(p)
        if p in g:
            s+=g[p]
    return False

def Krushkal(g,v,e):
    g = (sorted(g, key=lambda edge:edge[2]))
    res=[]
    counter_edge = 0
    track = {}
    cost=0
    while counter_edge<v-1:
        a,b,c = g.pop(0)
        if check(track,a,b) is False:
            res.append((a,b,c))
            cost+=c
            if a not in track:
                track[a] = [b]
            else:
                track[a].append(b)
            if b not in track:
                track[b] = [a]
            else:
                track[b].append(a)
            counter_edge+=1

    print(res,cost)


g,v,e=create()
Krushkal(g,v,e)
