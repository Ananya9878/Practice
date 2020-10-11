n = int(input())
arr = list(map(int,input().split()))
# l1=[]
# l2=[]
# for i in range(len(arr)-1):
#     if (arr[0] - arr[i]) <=1:
#         l1.append(arr[i])
#
#     if arr[i] not in l1 and abs(arr[0] - arr[i+1]) <=1:
#         l2.append(arr[i])
#
# print(l1)
# print(l2)
d={}
for i in arr:
    if i in d.keys():
        d[i]+=1
    else:
        d[i] = 1
print(d)
a=[]
for i in d.keys():
    c=d[i]
    c1=d[i]
    if i-1 in d:
        c+=d[i-1]
    if i+1 in d:
        c1+=d[i+1]
    a.append(c)
    a.append(c1)

print(max(a))








