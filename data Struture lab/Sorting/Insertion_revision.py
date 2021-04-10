l=[4,3,2,10,12,1,5,6]

for i in range(len(l)):
    j=i
    while l[j]>=l[i]:
        if j==0:
            k=l.pop(i)
            l.insert(0,k)
            break

        if l[i]>l[j-1]:
            t=l.pop(i)
            l.insert(j,t)
            break
        j-=1
print(l)



