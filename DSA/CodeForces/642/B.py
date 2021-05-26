for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b = sorted(b)[::-1]
    c=0
    for i in range(n):
        if b[i]>a[i] and c!=k:
            a[i] = b[i]
            c+=1
    print(sum(a))
