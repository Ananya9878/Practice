n,k=list(map(int,input().split()))
arr=list(map(int,input().split()))
b=int(input())
t = sum((arr))
w=t-(arr[k])
x = arr[k]//2
if w//2 == b:
    print('Bon Appetit')
else:
    q = b-w
    print(q)

