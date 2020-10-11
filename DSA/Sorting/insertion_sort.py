l=[6,2,9,1,3,4]
for i in range(1,len(l)):
    j = i
    while l[j] < l[j-1]:
        l[j],l[j-1] = l[j-1],l[j]
        j-=1
        if j == 0:
            break
print(l)

