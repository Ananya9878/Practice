def height(d,root,v):
    if root in v:
        return 0
    v.add(root)
    if root not in d:
        return 0
    m = 0
    for i in d[root]:
        a = height(d,i,v)
        if a > m:
            m = a
    return 1+m

n = int(input())
d={}
for i in range(1,n+1):
    a = int(input())
    # if a!= -1:
    if a not in d:
        d[a]=[i]
    else:
        d[a].append(i)
    # else:
v=set()
print(height(d,-1,v))

# visited = set()
# max_h = 0
# for i in d.keys():
#     if i not in visited:
#         h = height(d,i,visited)
#         if h>max_h:
#             max_h = h
# print(max_h)
# print(d)
# 2 2 -1
