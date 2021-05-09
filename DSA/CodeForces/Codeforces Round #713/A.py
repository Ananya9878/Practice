for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    a = list(set(arr))
    b,c = arr.count(a[0]),arr.count(a[1])
    if b>c:
        t = arr.index(a[1])
    else:
        t = arr.index(a[0])
    print(t+1)





