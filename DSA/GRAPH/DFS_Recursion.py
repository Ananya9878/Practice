c=0
def Dfs(visited,start,end,c):
    if start == 3:
        c+=1
        print('***')
    if start in visited:
        return c
    print(start)
    visited.add(start)
    for i in d[start]:
        c=Dfs(visited,i,end,c)
    return c

def Bfs(visited,start,end,c):
    pass



f = open('input.txt','r')
v,e = map(int,f.readline().split())
d={}
for i in range(e):
    a,b= map(int,f.readline().split())
    if a not in d:
        d[a] = [b]
    else:
        d[a].append(b)
    if b not in d:
        d[b] = [a]
    else:
        d[b].append(a)

visited = set()
c=Dfs(visited,2,3,0)
print(c)









