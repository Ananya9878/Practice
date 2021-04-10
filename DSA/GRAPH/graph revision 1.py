def list_adjl(l,v,e):
    d = {}
    for i in range(e):
        a,b,c = l[i]
        if a not in d:
            d[a] = [(b,c)]
        else:
            d[a].append((b,c))

        if b not in d:
            d[b] = [(a,c)]
        else:
            d[b].append((a,c))

    return d

def ad_mat(l,v,e):
    mat = [[0]*e for i in range(e)]
    for i in range(e):
        a,b,c = l[i]
        mat[a-1][b-1] = c
        mat[b-1][a-1] = c
    return mat


def  dfs_list(g,s):
    st = [(s,0)]
    visited = set()
    while len(st)>0:
        p = st.pop()

        if p[0] not in visited:
            visited.add(p[0])
            print(p)
            for i in g[p[0]]:
                st.append((i[0],i[1]+p[1]))
    return


def dfs_mat(g,s):
    st = [(s,0)]
    visited = set()
    while len(st)>0:
        p = st.pop()
        if p[0] in visited:
            continue
        else:
            visited.add(p[0])
        print(p)
        n = p[0]-1
        for i in range(len(g)):
            if g[n][i] != 0:
                st.append((i+1,g[n][i]+p[1]))
    return

def bfs_list(g,s):
    st = [(s,0)]
    visited = set()
    while len(st)>0:
        p = st.pop(0)
        if p[0] in visited:
            continue
        visited.add(p[0])
        print(p)
        for i in g[p[0]]:
            st.append((i[0],i[1]+p[1]))
    return

def bfs_mat(g,s):
    st = [(s,0)]
    visited = set()
    while len(st)>0:
        p = st.pop(0)
        if p[0] in visited:
            continue
        visited.add(p[0])
        print(p)
        l = g[p[0]-1]
        for i in range(len(l)):
            if l[i]!=0:
                st.append((i+1,l[i]+p[1]))
    return

def mini(st):
    m = st[0][1]
    m_i = 0
    for i in range(len(st)):
        if st[i][1]<m:
            m = st[i][1]
            m_i = i
    return st.pop(m_i)


def dijkhshta(g,s):
    st = [(0,s)]
    import heapq
    heapq.heapify(st)
    visited = set()
    while len(st)>0:
        p = heapq.heappop(st)
        if p[1] in visited:
            continue
        print(p)
        visited.add(p[1])
        for i in g[p[1]]:
            heapq.heappush(st,(i[1]+p[1],i[0]))
    return


def main():
    v,e = 6,8
    l = [(1,2,1),(1,3,1),(2,4,1),(3,5,1),(2,5,1),(3,4,1),(4,6,1),(5,6,1)]
    g1 = ad_mat(l,v,e)
    g2 = list_adjl(l,v,e)
    # dfs_list(g2,1)
    # dfs_mat(g1,1)
    # bfs_list(g2,1)
    # bfs_mat(g1,1)
    dijkhshta(g2,1)
if __name__ == '__main__':
    main()