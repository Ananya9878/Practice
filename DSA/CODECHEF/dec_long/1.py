d1,v1,d2,v2,p = list(map(int,input().split()))
a = min(d1,d2)
if a == d1:
    t = v1
else:
    t = v2
s = (abs(d1-d2))*(t)
if s>p:
    n = p//t
    if p%t != 0:
        n+=1
    print(a-1+n)
else:
    comA = p-s

    b = max(d1,d2)
    c = (comA)//(v1+v2)
    t = comA%(v1+v2)
    if t != 0:
        c+=1
    q = c
    print(abs(d1-d2)+q+a-1)



