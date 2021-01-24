for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    arr = arr[::-1]
    r1=0
    r2=0
    for i in range(2,n,1):
        if r1 > r2:
            r2+=arr[i]
        else:
            r1+=arr[i]
    print(max(r1,r2))







