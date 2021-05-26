def create():
    n = int(input())
    d={}
    for i in range(1,n):
        a = int(input())
        u,v = i+1,a
        if v not in d:
            d[v] = [u]
        else:
            d[v].append(u)
    return d

def check(d,root):
    c=0

    for i in d[root]:
        if i not in d:
            c+=1
    if c>=3:
        print('Yes')
    else:
        print('No')




d={}
d=create()
# print(d)
check(d,1)