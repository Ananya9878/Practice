n,k,q = list(map(int,input().split()))
arr=list(map(int,input().split()))
arr = arr[-k:]+arr[:-k]
q=[]
for i in range(len(arr)):
    m=int(input())
    q.append(arr[m])

    print(arr[m])


