l = list(map(int,input().split()))
# l = [1,1,1,1]
d={}
for i in range(len(l)):
    if l[i] in d:
        d[l[i]]+=1
    else:
        d[l[i]] = 1
s = set(l)
c=0
for i in range(len(l)):
    a = l[i]
    if a+1 in s:
        m = d[a]+d[a+1]
        if m>c:
            c=m

print(c)

