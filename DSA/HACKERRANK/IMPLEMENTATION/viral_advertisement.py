n=int(input())
l=[]
p = 5
for i in range(1,n+1):
    q = p//2
    s = q*3
    p = s
    l.append(q)
print(sum(l))
# print(sum(l))
