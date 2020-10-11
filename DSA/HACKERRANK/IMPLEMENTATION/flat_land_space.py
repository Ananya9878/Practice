n,m=100,90
arr = list(map(int,input().split()))
l=[]

arr.sort()
for i in range(1,len(arr)):
    x = abs(arr[i] - arr[i-1])
    if x%2 == 0:
        x = x//2
    else:
        x = x//2+1
    l.append(x)


print(max(l))

