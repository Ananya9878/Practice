mat = [[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]]
k = 2
l = []

for j in mat:
    a =j.count(1)
    l.append(a)

for i in range(len(l)):
    l[i] = (l[i],i)
l.sort()
p = [None]*k
for i in range(k):
    p[i] = l[i][1]

print(p)


