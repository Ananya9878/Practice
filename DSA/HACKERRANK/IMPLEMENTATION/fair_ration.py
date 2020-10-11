n=5
arr=[2,3,4,5,6]
a = len(arr)
c=0
flag = True
for i in range(a-1,-1,-1):
    
    if arr[i]%2 != 0:
        arr[i]=arr[i]+1
        arr[i-1]+=1
        c+=2
for i in arr:
    if i%2 != 0:
        flag = False
if flag:
    print(c)
else:
    print('No')

