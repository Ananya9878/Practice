# n=8
n = int(input())
l = list(map(int,input().split()))
d={}
# l = [1,1,2,2,3,2,5]
for i in range(1,len(l)+1):
    u,v= i+1,l[i-1]
    if v not in d:
        d[v] = [u]
    else:
        d[v].append(u)


def dfs(d,root,n,l,v):
    if root in v:
        return False
    else:
        v.add(root)
    if root == n:
        return True
    if root in d:
        for i in d[root]:
            a=dfs(d,i,n,l,v)
            if a is True:
                l.append(i)
                return  True
    return False


l=[]
a=dfs(d,1,n,l,set())
if a:
    l.append(1)
print(*l[::-1])
# 1 1 2 2 3 2 5
# 2 3 4 5 6 7 8
# 1:[2,3]




