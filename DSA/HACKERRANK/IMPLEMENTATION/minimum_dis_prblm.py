n = 6
arr=[7,1,3,4,1,7]
l=[]
for i in range(n):
    for j in range(i):
        if arr[i] == arr[j]:
            l.append(abs(i-j))
if len(l)==0:
    print(-1)
else:
    print(min(l))

