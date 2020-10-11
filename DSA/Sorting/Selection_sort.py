l=[6,2,9,1,3,4]
l1=[1,2,3,4,6,9]
def mini(l,start,end):
    m = l[start]
    k = start
    for i in range(start,end):
        if m > l[i]:
            m=l[i]
            k = i
    return k
start , end = 0 , len(l)
while start < len(l):
    k = mini(l,start,end)
    l[start],l[k] = l[k] , l[start]
    start+=1
print(l)

