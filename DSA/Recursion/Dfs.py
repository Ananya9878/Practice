f = open('input.txt','r')
v,e = map(int,f.readline().split())
g={}
for i in range(e):
    a,b,c = map(int,f.readline().split())
    if a not in g:
        g[a] = [b]
    else:
        g[a].append(b)
    if b not in g:
        g[b] = [a]
    else:
        g[b].append(a)



# def dfs(g,start,end):
#     s = [start]
#     visited = set()
#     while len(s)>0:
#         p = s.pop()
#         if p in visited:
#             continue
#         visited.add(p)
#         print(p)
#         if p in g:
#             for i in g[p]:
#                 s.append(i)
#
# dfs(g,0,3)
l=[]
def Dfs_recursion(g,visited,start,end):
    if start == end:
        # print(end)
        return True
    visited.add(start)
    # print(start)
    if start in g:
        p = g[start]
        for i in p:
            if i not in visited:
                t=Dfs_recursion(g,visited,i,end)
                if t:
                    l.append(i)
                return t
    return False

print(Dfs_recursion(g,set(),1,4))
print(l)













