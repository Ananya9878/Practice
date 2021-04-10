from collections import Counter
arr = [2,3,5,6,2,8]
k = 10
c=0
d = Counter(arr)
# print(d)
b = set(arr)
for i in range(len(arr)):
    t = k - arr[i]
    if t in d:
        if d[t]>0:
            d[t]-=1
            if d[arr[i]]>0:
                c+=1
                d[arr[i]]-=1
                print(d)
print(c)





