s='abccddde'
n=6
l=[]
d={}
l1=[]
for i in s:
    a = ord(i) - 96
    if i in d:
        d[i]+=1
        l.append(a*d[i])
    else:
        d[i]= 1
        l.append(a*d[i])
print(l)

for q in queries:
    if q in l:
        l1.append('Yes')
    else:
        l1.append('No')
print (l1)


