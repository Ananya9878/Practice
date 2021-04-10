def create(n):
    g={}
    for i in range(n-1):
        u,v = map(int,input().split())
        if u not in g:
            g[u] = [v]
        else:
            g[u].append(v)

    return g

def height(g,r,p):
    if r not in g:
        return 1
    max_h = 0
    for i in g[r]:
        h=(height(g,i,p))
        if max_h<h:
            max_h = h
    # p.append((r,1+max(l)))
    p[r] = 1+max_h
    return 1+max_h

def even(g,r,d):
    if r not in g:
        if r & 1:
            return 0
        else:
            return 1
    m=0
    for i in g[r]:
        h = even(g,i,d)
        m+=h
    if r &1==0:
        m+=1
    d[r] = m
    return m

def even_ancestor(g,r,m,d):
    if r not in g:
        d[r]=m
        if r & 1 == 0:
            m+=1
        # print(r,m)
        return m
    d[r] = m
    if r&1==0:
        m+=1

    for i in g[r]:
        even_ancestor(g,i,m,d)
    # print(r,m)
    return m

def even2(g,r,n,d):
    if r not in g:
        if r & 1:
            return 0
        else:
            return 1

    m=0
    if r&1==0:
        n+=1
    for i in g[r]:
        a=even2(g,i,n,d)
        m+=a
    # print(r, m, n)
    d[r]=m+n
    if r&1==0:
        m+=1

    # d[r]=m+n
    return m









def main():
    n = int(input())
    g = create(n)
    p={}
    d={}
    # print(height(g,1,p))
    # print(even(g,1,d))
    # print(d)
    # even_ancestor(g,1,0,d)
    even2(g,1,0,d)

    print(d)

if __name__ == '__main__':
    main()

#
# 10
# 1 2
# 1 3
# 2 4
# 2 5
# 4 8
# 4 9
# 5 10
# 3 6
# 3 7