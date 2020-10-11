n = int(input())
arr = list(map(int,input().split()))
c=0
i=0
while i<n-2:
    if arr[i+2] == 0:
        c+=1
        i+=2
    else:
        c+=1
        i+=1
if i != n-1:
    c+=1
print(c)


