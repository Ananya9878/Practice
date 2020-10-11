# p,d,m,s = map(int,input().split())
p,d,m,s = 100,1,1,99
l=[]
for i in range(p,m,-d):
    l.append(i)
while sum(l)+m <= s:
    l.append(m)
print(len(l))




