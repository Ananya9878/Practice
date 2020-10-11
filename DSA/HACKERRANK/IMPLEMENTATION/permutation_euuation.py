n=int(input())
arr=list(map(int,input().split()))
l=[]


for x in range(1,n+1):
    c=arr.index(x)+1

    l.append(arr.index(c)+1)
print(l)

