# def knapsack(arr,i,n,d):
#     if i>=n:
#         return 0
#     if i in d:
#         return d[i]
#     a = knapsack(arr,i+arr[i],n,d)+arr[i]
#     # b = knapsack(arr,i+1,n,d)
#     d[i] = a
#     return a


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    for i in range(n-1,-1,-1):
        if i+arr[i]<n:
            arr[i] = arr[i+arr[i]]+arr[i]
    print(max(arr))


