n,k = 5,3
arr = 4,2,6,1,10
c=0
l=[]
for i in arr:
    l1=[j for j in range(1,i+1)]
    for q in range(0,len(l1),k):
        s = l1[q:q+k]
        l.append(s)
print(l)
for i in range(len(l)):
    if i+1 in l[i]:
        c+=1

print(c)




