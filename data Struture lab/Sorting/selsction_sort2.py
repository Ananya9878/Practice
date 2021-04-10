l=[99]

def maxi(l,start,end):
    m = l[start]
    k = start
    for i in range(start,end+1):
        if m < l[i]:
            m = l[i]
            k = i
    return k
start , end = 0 , len(l)-1
while end > 0:
    k = maxi(l,start,end)
    l[end],l[k] = l[k] , l[end]
    end-=1
print(l)