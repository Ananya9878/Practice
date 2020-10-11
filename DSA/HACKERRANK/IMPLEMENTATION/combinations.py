l=[1,2,3,4,5]
k=6
l1=[]
d=set()
for i in range(len(l)):
    for j in range(len(l)):
        if i!=j and l[i]+l[j] == k and l[i] not in d and l[j] not in d:
            l1.append((l[i],l[j]))
            # d[l[i]] = 1
            # d[l[j]] = 1
            # d.append(l[i])
            # d.append(l[j])
            d.add(l[i])
            d.add(l[j])
print(l1)
