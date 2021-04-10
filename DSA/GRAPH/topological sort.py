def create(v,e):
    d = {}
    for i in range(e):
        a,b = map(int,input().split())
        if a not in d:
            d[a] = [b]
        else:
            d[a].append(b)
    return d

def dfs(d,visited,s,l):
    if s in visited:
        return
    visited.add(s)
    if s in d:
        for i in d[s]:
            dfs(d,visited,i,l)
    l.append(s)


def main():
    v, e = map(int, input().split())
    l = []
    g = create(v,e)
    visited = set()
    for i in range(1,v+1):
        if i not in visited:
            dfs(g,visited,i,l)
    print(l)
main()