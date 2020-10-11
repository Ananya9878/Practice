n,k = map(int,input().split())
arr=list(map(int,input().split()))
e=100
i=0
while 1:
    i = (i+k)%n
    if arr[i] == 1:
        a=e-1-2
    else:
        a = e-1
    e=a
    if i == 0:
        break
print(e)
