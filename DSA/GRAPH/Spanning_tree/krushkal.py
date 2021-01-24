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
    print(s)
    # print(s)
    visited = set()
    while len(s)>0:
        p = s.pop()
        if p == end:
            # print(p,'*')
            return True
        if p in visited:
            continue
        visited.add(p)

        if p in g:
            s+=g[p]
            # print(s,g[p])
    return False

def Krushkal(g,v,e):
    g = (sorted(g, key=lambda edge: edge[2]))
    print(g)
    res = []
    cost = 0
    edge_counter=0
    track = {}
    while edge_counter<v-1:
        a,b,c = g.pop(0)
        print((a,b,c),'*')
        if check(track,a,b) is False:
            res.append((a,b,c))
            cost += c
            if a in track:
                track[a].append(b)
            else:
                track[a] = [b]
            if b in track:
                track[b].append(a)
            else:
                track[b] = [a]
            edge_counter += 1

        # if a not in track or b not in track:
        #     res.append((a,b,c))
        #     cost+=c
        #     if a in track:
        #         track[a].append(b)
        #     else:
        #         track[a] = [b]
        #     if b in track:
        #         track[b].append(a)
        #     else:
        #         track[b] = [a]
        #     edge_counter += 1
        # else:
        #     if check(track,a,b):
        #         res.append((a,b,c))
        #         cost+=c
        #         track[a].append(b)
        #         track[b].append(a)
        #         edge_counter+=1
    print(res,cost)
    print(track)

g,v,e=create()
Krushkal(g,v,e)


